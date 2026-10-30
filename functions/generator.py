def sample():
    yield 2
    yield 1
    yield "python life"

obj=sample()
print(list(obj))#[2,1,'python life']
