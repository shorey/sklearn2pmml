from distutils.core import setup

setup(
	name = "sklearn2pmml",
	version = "0.9.3",
	description = "Python library for converting Scikit-Learn models to PMML",
	author = "Villu Ruusmann",
	author_email = "villu.ruusmann@gmail.com",
	url = "https://github.com/jpmml/sklearn2pmml",
	license = "GNU Affero General Public License (AGPL) version 3.0",
	packages = [
		"sklearn2pmml",
		"sklearn2pmml.decoration",
		"sklearn2pmml.resources"
	],
	package_data = {
		"sklearn2pmml.resources" : ["*.jar"]
	},
	install_requires = [
		"joblib",
		"numpy",
		"sklearn",
		"sklearn_pandas"
	]
)
