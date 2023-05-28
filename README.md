## Tripphrase
A tripphrase is a variant of a tripcode, which is used as a means for users to preserve their identity on platforms like 4chan and similar message boards. While a tripcode is a jumbled sequence of letters and numbers generated from a password, a tripphrase is a grammatically valid short phrase generated from a password. The tripphrase is more memorable, fun, and likely to be used compared to traditional tripcode.

Tripphrase address two main problems with tripcodes: their lack of usage and lack of attention. Tripphrase are more likely to be used because users can generate funny or interesting phrases, turning the process into a game. They can proudly display their tripphrases, demonstrating their achievement and possessing unique knowledge. Tripphrase are also more likely to be noticed because they are meaningful, making imposters more easily recognizable.

This script provides a simple way to generate tripphrases from secrets/passwords. It uses a set of predefined word templates and word sources to construct the tripphrases. The script generates a unique tripphrase for each secret, ensuring a diverse set of phrases.

## Prerequisites

To run this script, make sure you have Python installed on your system. The script is compatible with Python 3.

## Usage

You can execute the script using the following command:

```
python tripphrase_generator.py [secret]
```

### Arguments

- `secret` (optional): The secret to generate a tripphrase from. If not provided, a random secret will be generated.

## How it Works

1. The script first imports necessary modules and initializes some variables.
2. It defines a list of templates that specify the word order for the tripphrase.
3. The script checks if the required word types ("noun", "verb", "adj", "adv", "article") are valid.
4. It provides functions to retrieve words for each word type from corresponding text files. Words are cached to improve performance.
5. The script defines a function to generate a tripphrase based on a given password. The password is hashed using MD5, and the resulting hash is used to derive indexes.
6. The indexes are used to select a template and word types for the tripphrase.
7. Random words are selected for each word type, forming the tripphrase.
8. There is also a function to generate a random tripphrase without providing a secret.
9. Additionally, a function is defined to generate a random secret of a specified length.
10. The script uses the `argparse` module to parse command-line arguments. If a secret is provided as an argument, it is used; otherwise, a random secret is generated.
11. Finally, the tripphrase is printed to the console in the format `(<secret>) <tripphrase>`.

## Word Sources

The script requires word sources in the form of text files with one word per line. The word sources should be named following the word types (`noun.txt`, `verb.txt`, `adj.txt`, `adv.txt`, `article.txt`). These files should be present in the same directory as the script.

## Examples

- Generate tripphrase from a random secret:

  ```
  $ python tripphrase_generator.py
  ```

  Output:
  ```
  (random_secret) article verb adj noun
  ```

- Generate tripphrase from a specific secret:

  ```
  $ python tripphrase_generator.py my_secret
  ```

  Output:
  ```
  (my_secret) verb article adj noun
  ```

## Special Thanks
Special thanks to Bret Victor for the tripphrase algorithm reference, which inspired the development of a more memorable, fun, and user-friendly approach to preserving user identities on message boards.

## License

This script is released under the [MIT License](LICENSE).
