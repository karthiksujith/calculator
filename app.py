import streamlit as st

def add(a , b):
    return a + b
def sub(a , b):
    return a - b
def mul(a , b):
    return a * b
def mod(a , b):
    if b == 0:
        return 'Cannot calculate modulus by Zero'
    return a % b
def div(a , b):
    if b == 0:
        return 'Cannot divide by Zero'
    return a / b

operations = {
    'Addition': add,
    'Subtraction': sub,
    'Multiplication': mul,
    'Modulus': mod,
    'Division': div
}

st.title('My Calculator')
st.write('Simple calculator built with Python')

num_1 = st.number_input('First number', value=0.0)
num_2 = st.number_input('Second number', value=0.0)
operation = st.selectbox(
    'choose operation',
    list(operations.keys())
)

if st.button('calculate'):
    result = operations[operation](num_1 , num_2)
    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f'Result: {result:,.10g}')

