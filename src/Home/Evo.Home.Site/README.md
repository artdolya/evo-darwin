# Evo.Home.Site

The home site of Evo: a few static pages. It has no API, no worker and no database.

The site has one page today. It shows the text "Evolution starts here" on a full-page background. The pages are written by hand. No tool builds them.

The pages that are planned:

- Basic information about Evo.
- How to get the app from Google Play and from the App Store.

## Files

| File | Content |
| --- | --- |
| `index.html` | The page. Its styles are inside the file. |
| `favicon.svg` | The icon of the site: dots that grow along a spiral, on a dark tile. |
| `favicon.ico` | The same icon as a bitmap, at 16, 32 and 48 pixels, for browsers that do not show an SVG icon. |
| `background.svg` | The background of the page: a gradient that is stretched to the whole page, and the dots of the icon in its centre. The dots keep their shape at any page size. |

The page refers to the other files with relative paths, so it works from any folder and from any address.

No script in the repository creates `favicon.ico`. When `favicon.svg` changes, create `favicon.ico` again with an image tool. `background.svg` holds a copy of the dots of `favicon.svg`, at another scale. When the dots change, change both files.

## View locally

Open `index.html` in a browser. Or serve the folder, from the repository root:

```bash
python3 -m http.server 8080 --directory src/Home/Evo.Home.Site
```

Then open <http://localhost:8080>. Stop the server with `Ctrl+C`.

## Not decided

TODO: decide where the site is hosted and how it is deployed. No pipeline deploys it today.

TODO: decide whether the pages stay hand-written or are generated with a tool, before more pages are added.
