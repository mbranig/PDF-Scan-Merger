# PDF-Scan-Merger
A little script that merges scanned pdf files together, if you scan two-sided documents with a single-sided sheet feed scanner.

This is written and tested with python3.
To run the script, pdfrw and argparse must be installed.
You get help by using the argument `-h`.
Because the even pages will mostly be scanned in reverse order after you scanned the odd ones and turn the whole pile around, there is the `--evenrev` argument which reverses the even pages before shuffling them together. You can do this with odd pages (`--oddrev`), too.

In `examplefiles/` some example pdfs are provided to test the tool.

If you would like to have some additional features, feel free to contribute or create an issue.