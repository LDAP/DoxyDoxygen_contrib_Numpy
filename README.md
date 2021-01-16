
## DoxyDoxygen_contrib_Numpy

This plugin adds Numpy docstring style support to [DoxyDoxygen](https://github.com/20Tauri/DoxyDoxygen).

## Installation
- Install DoxyDoxygen via PackageControl
- Set the DoxyDoxygen settings to:

```json
{
    "preferred_comments_styles": [
        [
            "/**",
            " *"
        ],
        [
            ["/*", "-", "*//**"],
            " *"
        ],
        [
            ["//", "-"],
            "///"
        ],
        [
            "\"\"\"",
            [],
            "\"\"\""
        ],
        [
            "##",
            "##"
        ],
        [
            ["#", "-"],
            "##"
        ]
    ],
    "block_layout": {
        "Numpy": [
            "@_brief",
            "",
            "@_hidden_param_header",
            "@_hidden_param",
            "",
            "@_hidden_return_header",
            "@_hidden_return",
            "",
            "@_hidden_raises_header",
            "@_hidden_raises",
            ""
        ],
    },
    "profiles": [
        {
            "languages":  [ "python", "cython" ],
            "parsers":    [ "LanguagePython" ],
            "doc_styles": [ "DoxyDoxygen_contrib_Numpy" ]
        },
    ],
}
```