.. image:: https://bytebucket.org/emitc2h/sivega/raw/e55115b06e73953f2fbafa708884c9d52cf26d4a/logo.png?token=5a8b0da1aaff86b72545802873fd3540a4e3055e
   :scale: 25 %

| **project:** sivega 0.0
| **author:** Michel Trottier-McDonald <mtrottiermcdonald@lbl.gov>
| **creation date:** December 2014

**Project proposal:**

Sivega is a future python library providing full style control and flexibility for ROOT histogram
classes. It produces the graphical data directly into SVG, and uses the cairo engine to render
publication quality plots to more standard formats such as EPS, PDF and PNG. The SVG 1.1
specification is notorious for its universality and flexibility, and provides plotting capabilities
more powerful than the native ROOT rendering engine.

A secondary goal of sivega is to provide the user tools to quickly produce with a minimum
of user input, plots with the information strategically scaled, positioned and contrasted
for maximal visual ease.

Another goal is to preserve the ROOT data structure, such that operations on histograms can still
be done in the traditional way. However, sivega completely replaces the ROOT rendering engine, so
no more calls to ROOT's canvases, styles, and colors are necessary.

ROOT currently has the capability of converting its output to SVG, and is therefore very limited
in the opportunities that SVG offers. Sivega working with native SVG allows for easy interfacing
with HTML and XML, offering the tantalizing possibility of interactive plots on the web. It also
allows to produce lightweight SVG files which can be easily integrated and subsequently modified
in vector graphics editors such as Adobe Illustrator and Inkscape. Another exciting possibility
is the integration of MathML, which offers mathematical equation rendering on par with LateX for
plot labels.