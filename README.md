# CSS Ipsum

Simple, manageable placeholder content using pure CSS.

## How it works

1. Include `cssipsum.css` in your page
1. Add the `ipsum` attribute to your element: `<p ipsum>` or `<p ipsum='30'>`

The placeholder content will be inserted using CSS `:after`, which means you do not need to alter your markup. To remove the placeholder content, simply stop including the CSS file.

## Why use it

* You can enable/disable/change placeholder content across the entire site in a pinch
* You can disable placeholder content server-side by omitting the CSS file
* You can remove all placeholders with a simple find/replace
* It took me 10 minutes to build it, so you don't feel bad about not having a use for it

## Use your own placeholder content

You can edit and re-run generate.py to use your own placeholder content or change which attribute to use to activate CSS Ipsum.