# Version comparison test suite

![CI](https://github.com/repology/version-comparison-test-suite/workflows/CI/badge.svg)

This is a comprehensive test suite for version string comparison
algorithms primary developed for
[libversion](https://github.com/repology/libversion), advanced
version string comparison library, extracted and generalized to
be suitable for using with version comparison algorithm/library.

The suite is maintained in the form of text file, containing test
cases in the following format:

```
"1.0.1" < "1.0.2"
```

which consists of two quoted version strings and an relation sign
denoting expected comparison result. The test suite is also split
into sections and test cases may contain additional implementation
defined flags which affect comparison.

See [the test suite](version-comparison-tests.txt) for complete
info on format.

## Author

* [Dmitry Marakasov](https://github.com/AMDmi3) <amdmi3@amdmi3.ru>

## License

* [CC0](LICENSE)
