# Passw0rd

The project consists of a password generator, which aims to help users use
more secure passwords in their accounts. Avaliable in pypi.

## Installation

Install passw0rd with pip

```bash
  pip install passw0rd
```

## Documentation

The following documentation explains how to use each of the functions
included in this package.

### generate_pwd()

```python
generate_pwd(length=64, characters=characters)
```

The generate_pwd() function accepts arguments length and characters. The length, as
the name says, indicates how long you want your password to be. As default the value
is 64, we do not recommend changing it, due to the security the actual value provides.
The characters argument gives the function the specific characters to use for creating
the password, you can use whatever you want. By default characters = characters,
a variable that include upcase and lowercase letters, 0-9 numbers and symbols.

### is_secure()

```python
is_secure(pwd: str)
```

The is_secure function just accept a mandatory argument called 'pwd', refering to the
actual password to be tested. The argument must be of type 'str'. It will return a string
telling you how secure the password is.
