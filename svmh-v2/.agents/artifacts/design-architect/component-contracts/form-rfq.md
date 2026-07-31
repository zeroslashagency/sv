# Contract — `.form` (RFQ / contact)

**Status:** shipped. Highest-risk component on the site: it collects data and it is the conversion point.

## HTML skeleton

```html
<form class="form" action="/rfq" method="post" novalidate>
  <ol class="form__step-track" aria-label="Quote request progress">
    <li class="form__step form__step-current" aria-current="step">01 · Your requirement</li>
    <li class="form__step">02 · Site &amp; duty</li>
    <li class="form__step">03 · Contact</li>
  </ol>

  <fieldset class="form__group">
    <legend class="form__legend">Your requirement</legend>

    <div class="form__field">
      <label class="form__label" for="crane-type">Crane type</label>
      <select class="form__select" id="crane-type" name="crane_type" required>
        <option value="">Select a type</option>
        <option value="single-girder">Single-girder EOT</option>
        <option value="double-girder">Double-girder EOT</option>
        <option value="gantry">Gantry / goliath</option>
        <option value="jib">Jib</option>
        <option value="hoist">Hoist only</option>
        <option value="spares">Spares / service</option>
      </select>
      <p class="form__hint" id="crane-type-hint">Not sure? Pick the closest and describe the lift below.</p>
      <p class="form__error" id="crane-type-error" hidden>Select a crane type.</p>
    </div>

    <div class="form__row">
      <div class="form__field">
        <label class="form__label" for="capacity">Capacity (T)</label>
        <input class="form__input" id="capacity" name="capacity" type="number" min="0.5" max="500" step="0.5" inputmode="decimal">
      </div>
      <div class="form__field">
        <label class="form__label" for="span">Span (m)</label>
        <input class="form__input" id="span" name="span" type="number" min="1" max="60" step="0.5" inputmode="decimal">
      </div>
    </div>
  </fieldset>

  <fieldset class="form__group">
    <legend class="form__legend">Contact</legend>

    <div class="form__field">
      <label class="form__label" for="phone">Phone</label>
      <input class="form__input" id="phone" name="phone" type="tel" inputmode="tel"
             autocomplete="tel" required
             aria-describedby="phone-hint" aria-invalid="false">
      <p class="form__hint" id="phone-hint">Indian mobile or landline with STD code.</p>
      <p class="form__error" id="phone-error" hidden>Enter a valid Indian phone number.</p>
    </div>

    <div class="form__check">
      <input id="consent" name="consent" type="checkbox" required>
      <label for="consent">You may contact me about this enquiry.</label>
    </div>
  </fieldset>

  <div class="form__trap" aria-hidden="true">
    <label for="company-url">Company URL</label>
    <input id="company-url" name="company_url" type="text" tabindex="-1" autocomplete="off">
  </div>

  <div class="form__actions">
    <button class="btn btn--primary" type="submit">Send enquiry<span class="btn__glyph" aria-hidden="true">↗</span></button>
  </div>

  <p class="form__status" role="status" aria-live="polite"></p>
  <p class="form__note">Drawings and load-cycle details can follow by email — send the enquiry first and we will reply with what we still need.</p>
</form>
```

## Progressive enhancement — mandatory

`.form__group` fieldsets ship **visible**. The form-steps JS module adds `hidden` to all but the first group on init and drives `.form__step-current`. With JS disabled the form is one long page that still submits. Shipping groups pre-hidden makes the form unusable without JS.

## Validation contract

| Aspect | Contract |
|---|---|
| Engine | Constraint Validation API. `novalidate` on the form so the module owns messaging, but native constraints (`required`, `type`, `min`, `max`, `pattern`) stay on the inputs — they are the fallback when JS is off. |
| Phone | `/^(?:\+91\|0)?[6-9]\d{9}$/` |
| Error display | `.form__error` unhidden, `aria-invalid="true"` on the input, `aria-describedby` extended to include the error `id`, `.form__field--error` on the field wrapper. |
| Error copy | States what to do ("Enter a valid Indian phone number"), never "Invalid input". |
| First error | Focus moves to the first invalid field on submit attempt. |
| Status | `.form__status` with `role="status" aria-live="polite"`, `--ok` / `--error` modifiers. Announces the submission result, not per-keystroke validation. |
| Timing | Validate on `blur` and on submit. Never on every keystroke. |

## Security requirements — read before wiring the endpoint

The honeypot `.form__trap` is a spam speed bump, **not** security. Whatever endpoint receives this form must have:

1. **Server-side validation** of every field. Client validation is a UX affordance only and is trivially bypassed.
2. **Rate limiting** per IP and per phone number.
3. **HTTPS-only POST**; no query-string submission of contact data.
4. **No secrets in client code** — no API keys, no SMTP credentials, no webhook tokens in the HTML or JS.
5. **Output encoding** wherever submitted data is later displayed (admin inbox, email template).

The JS module must never use `innerHTML` / `insertAdjacentHTML` / `eval`; error and status text is set with `textContent` only. Injecting a user-supplied value into the DOM as HTML would turn this form into a stored-XSS vector.

**Open item for the Orchestrator:** the build is a static site with no server named in the brief. Until an endpoint with the above controls exists, the submit button should point at a form service that provides them, or the form should degrade to `mailto:`/phone with the fields as a checklist. Do not ship a POST to an endpoint that has not been confirmed. This is recorded as a risk in `handoff-notes.md`.

## Accessibility

- Every control has a real `<label for>`. No placeholder-as-label.
- `<fieldset>` + `<legend>` group related fields; the legend is the group name shown in the step track.
- `autocomplete` on name, `tel`, `email`, `organization` — required for assistive tech and for basic courtesy.
- `inputmode` set for numeric and telephone fields so mobile keyboards are correct.
- Required fields carry `required`; the label states requirement in text if the visual marker is an asterisk.
- The honeypot is `aria-hidden="true"`, `tabindex="-1"`, `autocomplete="off"`, and positioned off-screen by CSS — never `display:none` on the input alone if the label remains focusable.
- Step track is an `<ol>` with `aria-current="step"` on the active item.
- Consent checkbox is opt-in, unchecked by default. Never pre-checked.
- Submit is a `<button type="submit">`, never a styled `<div>` or `<a>`.
- Touch targets ≥44px; `.form__input` height already satisfies this.

## Review gates

- [ ] Groups ship visible; JS hides on init.
- [ ] Every input has `<label for>` and, where relevant, `autocomplete` + `inputmode`.
- [ ] Native constraints present alongside `novalidate`.
- [ ] Error nodes exist in source with `hidden`, wired via `aria-describedby`.
- [ ] `.form__status` has `role="status" aria-live="polite"`.
- [ ] Honeypot off-screen, `aria-hidden`, `tabindex="-1"`.
- [ ] Consent unchecked by default.
- [ ] No secrets in client code; no `innerHTML` in the module.
- [ ] Endpoint confirmed with server-side validation, rate limiting and HTTPS — or form degraded, with the decision documented.
- [ ] Form submits and is fully usable with JS disabled.
