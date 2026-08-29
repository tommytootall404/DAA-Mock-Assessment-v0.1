# DAA Trainer

A timed practice app for the Royal Navy Defence Aptitude Assessment. 496 questions across the six
DAA sections, drawn at random so no two sittings are the same.

## Files

| File | What it is |
|---|---|
| `index.html` | The app. Open it in a browser. Never needs editing to add questions. |
| `questions.js` | The question bank the app reads. This is the file to edit or extend. |
| `questions.json` | The same bank in plain JSON, for anything else you want to do with it. |
| `build_questions.py` | Regenerates both files from scratch. Only needed if you change the generator. |

## Running it

Put all four files in one folder and double-click `index.html`. That's it — no install, no server,
no internet connection needed (it will fall back to system fonts if offline).

## What it does

- **Full mock** — all six sections back to back, 122 questions, about 62 minutes.
- **Section drill** — one section on its own, for working on a weak area.
- Per-section countdown. When it hits zero the section ends and unanswered questions score zero.
- Answers lock the moment they're chosen. No changing your mind, no going back a question,
  no returning to a finished section, no running score during the test.
- Results give a percentage per section, then every wrong answer with an explanation.
- Answer with the mouse or the number keys 1–4.

## Changing the timings or question counts

Open `index.html` and find the `CONFIG` block near the top of the script (around line 240).
Each section has a `count` (questions per sitting) and `seconds` (for the whole section):

```js
{key:"workrate", name:"Work Rate", count:24, seconds:360, blurb:"..."},
```

The MoD doesn't publish exact per-section timings, so these are estimates: roughly 30 seconds a
question, and 15 seconds for work rate. Tighten them as he gets faster.

## Adding questions

Edit `questions.js` directly. Each entry looks like this:

```js
{
 "id": "mech-071",
 "section": "mechanical",
 "question": "A force of 400 N acts on an area of 0.2 m². What is the pressure?",
 "options": ["2,000 Pa", "80 Pa", "200 Pa", "4,000 Pa"],
 "answer": 0,
 "explanation": "Pressure = force ÷ area = 400 ÷ 0.2 = 2,000 Pa."
}
```

`section` must be one of `verbal`, `numerical`, `workrate`, `spatial`, `mechanical`, `electrical`.
`answer` is the index of the correct option, counting from 0. `passage` is optional and renders
above the question — used for verbal reasoning. Basic HTML (`<b>`, `<i>`, `<br>`) works in the
question and passage text.

Alternatively edit `build_questions.py` and re-run it, which rebuilds both data files and re-checks
every question for duplicate options and bad answer indices.

## Hosting it

Any static host will do, since everything runs in the browser:

- **Netlify Drop** — go to app.netlify.com/drop and drag the folder in. Live in about 30 seconds.
- **Cloudflare Pages** or **GitHub Pages** — same idea, both free for a static folder.

Once it's hosted he can open it on any device, which matters because the real assessment must be
sat on a screen of at least 10.2 inches.

## A note on realism

The section structure and the constraints are modelled on the published description of the DAA.
The questions are written in the same style, but they are not the real thing and the timings are
estimates. Use the official familiarisation questions on the Royal Navy site as the reference for
format, and this app for volume and pressure.
