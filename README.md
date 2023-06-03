# XML Parser

This is a Python script for parsing XML files and extracting HOST:USER:PASS information. It provides two options: collecting the HOST:USER:PASS data and decoding passwords from base64 encoding.

## Features

- Collects HOST:USER:PASS information from XML files
- Decodes passwords from base64 encoding
- Customizable directory path for searching XML files

## Requirements

- Python 3.x
- base64 module (included in Python standard library)

## Usage

1. Clone the repository or download the `file.py` script.
2. Open a terminal and navigate to the directory containing `file.py`.
3. Run the script using the following command:
```
python file.py

```

4. Follow the on-screen instructions to select the desired option and provide the directory path for XML file search.

## Example
```
-- XML Parser --

Collect HOST:USER:PASS
Collect HOST:USER:PASS and decode passwords from base64
Enter your choice: 2
Enter the directory path: /

:::<delegatedecode="pdf"encode="eps"mode="bi"command=""gs"-sstdout=%%stderr-dQUIET-dSAFER-dBATCH-dNOPAUSE-dNOPROMPT-dMaxBitmap=500000000-dAlignToPixels=0-dGridFitTT=2"-sDEVICE=eps2write""-sPDFPassword=%a""-sOutputFile=%o""-f%i""/>
:::<delegatedecode="pdf"encode="ps"mode="bi"command=""gs"-sstdout=%%stderr-dQUIET-dSAFER-dBATCH-dNOPAUSE-dNOPROMPT-dMaxBitmap=500000000-dAlignToPixels=0-dGridFitTT=2"-sDEVICE=ps2write""-sPDFPassword=%a""-sOutputFile=%o""-f%i""/>
```

## Contribution

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This script is licensed under the [MIT License](LICENSE).
