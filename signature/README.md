# Email signature

Three files, one decision.

| File | Use it when |
|---|---|
| `signature.html` | **Default.** Paste into Gmail's signature editor. Nothing to host, nothing to block |
| `signature.txt` | Plain-text clients, or anywhere HTML gets stripped |
| `signature-mark.png` | Optional — the real handwritten mark, if you want it above the text |

## Why the default has no image

The brand mark is Caveat, and **no mail client will load Caveat.** Gmail,
Outlook and Apple Mail all strip `@font-face`. So the mark either becomes an
image or it falls back to something else.

`signature.html` falls back to **italic Georgia** — which is exactly what your
own `favicon.svg` already declares (`font-family="Caveat, Georgia, serif"`). It's
the documented fallback, it's on every machine, and it never breaks.

The image version looks better when it loads. It just doesn't always load:
plenty of corporate clients block remote images by default, and Outlook shows a
grey placeholder box where your name should be. That's a worse first impression
than Georgia.

**Use the text version day to day. Use the image version for pitch emails** where
you know the recipient and the client.

## Installing it in Gmail

1. Open `signature.html` in a browser
2. Select the rendered signature and copy it — not the source, the rendered
   version
3. Gmail → **Settings** → **See all settings** → **General** → **Signature**
4. Paste, and set it as the default for new mail and replies

Gmail keeps the inline styles and drops nothing, because there's nothing in
there it needs to strip — no `<style>` block, no classes, no external anything.

## Adding the mark, if you want it

Host `signature-mark.png` somewhere permanent — `public/img/` in the
entrepreneurcoach site repo is the obvious place, so it ships with the site —
then put this above the name row and delete the Georgia name row:

```html
<tr>
  <td style="padding:0 0 6px 0;">
    <img src="https://www.entrepreneurcoach.co.za/img/signature-mark.png"
         width="138" alt="Johannes le Roux"
         style="display:block;border:0;outline:none;text-decoration:none;">
  </td>
</tr>
```

`width="138"` renders the 415px image at a third of its size, so it stays sharp
on retina. **Always set `alt="Johannes le Roux"`** — that's what shows when the
image is blocked, and it means a blocked image still reads as your name.

## Changing it

Colours and type come from `DESIGN.md` in `getluckyjo/entrepreneurcoach`.
Vermilion is `#F25C2A`, ink is `#0E0E10`, muted is `#6F6F73`. If the brand
changes there, change it here second.

Regenerate the mark with `./scripts/build-signature.py`.

## One maintenance note

The last row of `signature.html` is the workshop offer. **Delete it when the
cohort is full**, or swap the detail for the next one. A signature advertising a
date that's passed is worse than a signature with no offer in it.
