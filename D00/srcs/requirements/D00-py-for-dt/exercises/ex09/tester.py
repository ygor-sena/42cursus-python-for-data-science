# Package website:
# https://pypi.org/project/ft-yde-goes-package/

# Source files v0.0.2:
# https://files.pythonhosted.org/packages/ca/f8/1a26da6a5e7121df01d7e0ed76a877ba37913351cb34a5ca01a7ce870dd2/ft_yde_goes_package-0.0.2.tar.gz
# https://files.pythonhosted.org/packages/a3/7d/c1a59bc4c54cebfcaed5844da811974228111928c3105908c01640dfb181/ft_yde_goes_package-0.0.2-py3-none-any.whl

from ft_yde_goes_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
