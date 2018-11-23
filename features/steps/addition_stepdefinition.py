from behave import given, when, then
from utility.addition import Calculator


@given(u'I have entered {num1:d} into the calculator')
def step_impl(context, num1):
    context.num1 = num1


@given(u'I have also entered {num2:d} into the calculator')
def step_impl(context, num2):
    context.num2 = num2


@when(u'I press add')
def step_impl(context):
    context.calc = Calculator()
    context.result = context.calc.add(context.num1, context.num2)


@then(u'the sum should be {result:d}')
def step_impl(context, result):
    assert context.result == result
