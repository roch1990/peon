from peon.src.lint.principles.definition.no_code_in_constructors import NoCodeInConstructor
from peon.src.lint.principles.definition.no_getters_and_setters import NoGettersAndSetters
from peon.src.lint.principles.definition.no_null import NoNull
from peon.src.lint.report.report import Report
from peon.src.lint.principles.definition.no_inheritance import NoInheritance
from peon.src.lint.principles.definition.no_instance_of_or_type_casting import NoInstanceOfOrTypeCastingOrReflection
from peon.src.lint.principles.definition.no_mutable_objects import NoMutableObjects
from peon.src.lint.principles.definition.no_readers_parsers_and_so_on import \
    NoReadersParsersOrControllersOrSortersAndSoOn
from peon.src.lint.principles.definition.no_statements_in_test_methods_except_assert import \
    NoStatementsInTestMethodsExceptAssert
from peon.src.lint.principles.definition.no_static_methods_and_not_even_private_ones import \
    NoStaticMethodsAndNotEvenPrivateOnes


class Principle:

    def __init__(
            self,
            files: tuple,
            output_channel: str,
    ):
        self.files = files
        self.output_channel = output_channel

    def no_null(self) -> Report:
        principle = NoNull(
            files=self.files,
            output_channel=self.output_channel,
        )
        return principle.check_rule()

    def no_code_in_constructors(self) -> Report:
        principle = NoCodeInConstructor(
            files=self.files,
            output_channel=self.output_channel,
        )
        return principle.check_rule()

    def no_getters_and_setters(self) -> Report:
        principle = NoGettersAndSetters(
            files=self.files,
            output_channel=self.output_channel,
        )
        return principle.check_rule()

    def no_mutable_objects(self) -> Report:
        principle = NoMutableObjects(
            files=self.files,
            output_channel=self.output_channel,
        )
        return principle.check_rule()

    def no_readers_parsers_or_controllers_or_sorters_and_so_on(self) -> Report:
        principle = NoReadersParsersOrControllersOrSortersAndSoOn(
            files=self.files,
            output_channel=self.output_channel,
        )
        return principle.check_rule()

    def no_static_methods_and_not_even_private_ones(self) -> Report:
        principle = NoStaticMethodsAndNotEvenPrivateOnes(
            files=self.files,
            output_channel=self.output_channel,
        )
        return principle.check_rule()

    def no_instanceof_or_type_casting_or_reflection(self) -> Report:
        principle = NoInstanceOfOrTypeCastingOrReflection(
            files=self.files,
            output_channel=self.output_channel,
        )
        return principle.check_rule()

    def no_public_methods_without_a_contract_interface(self):
        pass

    def no_statements_in_test_methods_except_assert(self) -> Report:
        principle = NoStatementsInTestMethodsExceptAssert(
            files=self.files,
            output_channel=self.output_channel,
        )
        return principle.check_rule()

    def no_orm(self):
        pass

    def no_inheritance(self) -> Report:
        principle = NoInheritance(
            files=self.files,
            output_channel=self.output_channel,
        )
        return principle.check_rule()
