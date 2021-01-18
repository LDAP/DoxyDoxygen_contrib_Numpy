"""
author: Lucas Alber <lucasd.alber@gmail.com>
"""

import re

__license__ = (
    "https://raw.githubusercontent.com/LDAP/DoxyDoxygen_contrib_Numpy/master/LICENSE.md"
)

param_header = "Parameters\n----------"
return_header = "Returns\n-------"
raises_header = "Raises\n------"

COMMANDS_LIST = [
    DoxyCommand(
        "@_hidden_param",
        "<parameter_name> : { parameter_type }\n    { parameter_description }",
        key_index=0,
    ),
    DoxyCommand(
        "@_hidden_return",
        "{ return_value_type }\n    { description_of_the_return_value }",
    ),
    DoxyCommand(
        "@_hidden_raises",
        "{ exception_object }\n    { exception_description }",
        key_index=0,
    ),
    DoxyCommand("@_hidden_param_header", "<workaround>" + param_header),
    DoxyCommand("@_hidden_return_header", "<workaround>" + return_header),
    DoxyCommand("@_hidden_raises_header", "<workaround>" + raises_header),
]


class DocStyle(DocStyleBase):
    name = "Numpy"

    typename_to_decorated = {
        EvaluatorBase.TYPE_STRING: "str",
        EvaluatorBase.TYPE_INTEGER: "int",
        EvaluatorBase.TYPE_BOOLEAN: "bool",
        EvaluatorBase.TYPE_FLOAT: "float",
        EvaluatorBase.TYPE_ARRAY: "Array",
        EvaluatorBase.TYPE_THIS: "Object",
    }

    def __init__(self):
        super().__init__(COMMANDS_LIST)

    def definition_to_commands_list(self, definition):
        def decorated_type(typename):
            return self.decorated_type(typename, DocStyle.typename_to_decorated, "%s")

        commands_list = []

        if definition["params"]:
            commands_list += self.command("@_hidden_param_header", [""])
            for param in definition["params"]:
                commands_list += self.command(
                    "@_hidden_param", [param.name, decorated_type(param.typename)]
                )

        definition_return = definition["return"]
        if (
            definition_return
            and definition_return != "void"
            and definition_return != "None"
        ):
            commands_list += self.command("@_hidden_return_header", [""])
            commands_list += self.command("@_hidden_return", [decorated_type(definition_return)])

        if definition["throws"]:
            commands_list += self.command("@_hidden_raises_header", [""])
            for type_name in definition["throws"]:
                commands_list += self.command(
                    "@_hidden_raises", [type_name]
                )

        return commands_list

    def generable_commands_names(self):
        return [
            "@_hidden_param",
            "@_hidden_return",
            "@_hidden_raises",
            "@_hidden_param_header",
            "@_hidden_return_header",
            "@_hidden_raises_header",
        ]

    def uncommented_text_to_lines(self, uncommented_text):
        """
        Implements a custom DocBlock parser for this DocStyle (all plugins that use
        hidden commands have to implement this method)

        Parameters
        ----------
        uncommented_text : str
            The text of the DocBlock whose the comment introducers have been
            removed

        Returns
        -------
        list
            The list of detected lines. A line is composed of 2 items.
            The first item is the name of the detected command.
            The second is the list of arguments for this command (each argument is a string or None if the value is yet to be determined)

        Examples
        --------
        >>> uncommented_text = ""
        >>> uncommented_text += "Build indices specifying all the Cartesian products of Chebychev\n"
        >>> uncommented_text += "polynomials needed to build Smolyak polynomial\n"
        >>> uncommented_text += ""
        >>> uncommented_text += "Parameters\n"
        >>> uncommented_text += "----------\n"
        >>> uncommented_text += "    x : type\n"
        >>> uncommented_text += "    Description of parameter `x`.\n"
        >>> uncommented_text += "    y\n"
        >>> uncommented_text += "    Description of parameter `y` (with type not specified).\n"
        >>> uncommented_text += "\n"
        >>> doc_style.uncommented_text_to_lines(uncommented_text)
        [
            ('@_brief', [' ']),
            ('@_brief', ['Build indices specifying all the Cartesian products of Chebychev polynomials needed to build Smolyak polynomial ']),
            ('@_hidden_Parameters_Header', ['']),
            ('@_hidden_Parameters_Header', ['Parameters']),
            ('@_hidden_Parameters_Header', ['----------']),
            ('@_hidden_Parameter', ['x', 'type', 'Description of parameter `x`.']),
            ('@_hidden_Parameter', ['y', None, 'Description of parameter `y` (with type not specified).']),
        ]
        """
        pass  # todo
