# 🎮 Polyglot README Tic-Tac-Toe

Welcome to the **14-language Tic-Tac-Toe** technical demonstration. This repository showcases how **GitHub Actions** can be used across multiple programming languages to maintain a unified game state directly in a README.

Each section below represents an independent implementation. Clicking a move link **[___]** will open a GitHub Issue — simply submit it to trigger the corresponding workflow and update the board!

---

## Python

<!-- PYTHON_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Python+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Python+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Python+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Python%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Python+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- PYTHON_END -->

<details>
<summary>📄 Python implementation snippet</summary>

```python
import os
import json

def main():
    lang = os.getenv("LANG_KEY") # "python"
    cell = os.getenv("CELL")      # e.g. "A1"
    # parse game_state.json, apply move, write back
    # full impl in implementations/python/game.py
```

</details>

---

## JavaScript

<!-- JAVASCRIPT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+JavaScript+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+JavaScript+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+JavaScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=JavaScript%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+JavaScript+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- JAVASCRIPT_END -->

<details>
<summary>📄 JavaScript implementation snippet</summary>

```javascript
const fs = require('fs');

const lang = process.env.LANG_KEY; // "javascript"
const cell = process.env.CELL;     // e.g. "A1"
// parse game_state.json, apply move, write back
// full impl in implementations/javascript/game.js
```

</details>

---

## TypeScript

<!-- TYPESCRIPT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+TypeScript+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+TypeScript+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+TypeScript+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=TypeScript%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+TypeScript+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- TYPESCRIPT_END -->

<details>
<summary>📄 TypeScript implementation snippet</summary>

```typescript
import * as fs from 'fs';

const lang = process.env.LANG_KEY; // "typescript"
const cell = process.env.CELL;
// parse game_state.json, apply move, write back
// full impl in implementations/typescript/game.ts
```

</details>

---

## Go

<!-- GO_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Go+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Go+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Go+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Go%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Go+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- GO_END -->

<details>
<summary>📄 Go implementation snippet</summary>

```go
package main
import "os"

func main() {
    lang := os.Getenv("LANG_KEY") // "go"
    cell := os.Getenv("CELL")
    // parse game_state.json, apply move, write back
    // full impl in implementations/go/game.go
}
```

</details>

---

## Rust

<!-- RUST_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Rust+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Rust+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Rust+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Rust%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Rust+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- RUST_END -->

<details>
<summary>📄 Rust implementation snippet</summary>

```rust
use std::env;

fn main() {
    let lang = env::var("LANG_KEY").unwrap(); // "rust"
    let cell = env::var("CELL").unwrap();
    // parse game_state.json, apply move, write back
    // full impl in implementations/rust/src/main.rs
}
```

</details>

---

## Java

<!-- JAVA_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Java+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Java+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Java+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Java%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Java+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- JAVA_END -->

<details>
<summary>📄 Java implementation snippet</summary>

```java
public class Game {
    public static void main(String[] args) {
        String lang = System.getenv("LANG_KEY"); // "java"
        String cell = System.getenv("CELL");
        // parse game_state.json, apply move, write back
        // full impl in implementations/java/Game.java
    }
}
```

</details>

---

## Kotlin

<!-- KOTLIN_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Kotlin+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Kotlin+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Kotlin+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Kotlin%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Kotlin+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- KOTLIN_END -->

<details>
<summary>📄 Kotlin implementation snippet</summary>

```kotlin
fun main() {
    val lang = System.getenv("LANG_KEY") // "kotlin"
    val cell = System.getenv("CELL")
    // parse game_state.json, apply move, write back
    // full impl in implementations/kotlin/Game.kt
}
```

</details>

---

## PHP

<!-- PHP_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+PHP+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+PHP+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+PHP+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=PHP%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+PHP+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- PHP_END -->

<details>
<summary>📄 PHP implementation snippet</summary>

```php
<?php
$lang = getenv("LANG_KEY"); // "php"
$cell = getenv("CELL");
// parse game_state.json, apply move, write back
// full impl in implementations/php/game.php
```

</details>

---

## Ruby

<!-- RUBY_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Ruby+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Ruby+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Ruby+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Ruby%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Ruby+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- RUBY_END -->

<details>
<summary>📄 Ruby implementation snippet</summary>

```ruby
lang = ENV['LANG_KEY'] # "ruby"
cell = ENV['CELL']
# parse game_state.json, apply move, write back
# full impl in implementations/ruby/game.rb
```

</details>

---

## C#

<!-- CSHARP_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C%23+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C%23+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C%23+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%23%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C%23+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- CSHARP_END -->

<details>
<summary>📄 C# implementation snippet</summary>

```csharp
using System;
using System.IO;

class Game {
    static void Main() {
        string lang = Environment.GetEnvironmentVariable("LANG_KEY"); // "csharp"
        string cell = Environment.GetEnvironmentVariable("CELL");
        // parse game_state.json, apply move, write back
        // full impl in implementations/csharp/Program.cs
    }
}
```

</details>

---

## C

<!-- C_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- C_END -->

<details>
<summary>📄 C implementation snippet</summary>

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    const char* lang = getenv("LANG_KEY"); // "c"
    const char* cell = getenv("CELL");
    // parse game_state.json, apply move, write back
    // full impl in implementations/c/game.c
    return 0;
}
```

</details>

---

## C++

<!-- CPP_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+C+++board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+C+++board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+C+++board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=C++%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+C+++board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- CPP_END -->

<details>
<summary>📄 C++ implementation snippet</summary>

```cpp
#include <iostream>

int main() {
    std::string lang = std::getenv("LANG_KEY"); // "cpp"
    std::string cell = std::getenv("CELL");
    // parse game_state.json, apply move, write back
    // full impl in implementations/cpp/game.cpp
    return 0;
}
```

</details>

---

## Scala

<!-- SCALA_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Scala+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Scala+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Scala+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Scala%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Scala+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- SCALA_END -->

<details>
<summary>📄 Scala implementation snippet</summary>

```scala
object Game extends App {
    val lang = sys.env("LANG_KEY") // "scala"
    val cell = sys.env("CELL")
    // parse game_state.json, apply move, write back
    // full impl in implementations/scala/Game.scala
}
```

</details>

---

## Swift

<!-- SWIFT_START -->
|   | A | B | C |   |
|---|---|---|---|---|
| **1** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A1&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B1&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C1&body=Play+Swift+board) | **1** |
| **2** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A2&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B2&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C2&body=Play+Swift+board) | **2** |
| **3** | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+A3&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+B3&body=Play+Swift+board) | [___](https://github.com/tdnb2b2/polyglot-readme-tictactoe/issues/new?title=Swift%3A+Tic-Tac-Toe%3A+Put+C3&body=Play+Swift+board) | **3** |
|   | A | B | C |   |

Turn: ❌ **X** is next

<!-- SWIFT_END -->

<details>
<summary>📄 Swift implementation snippet</summary>

```swift
import Foundation

let lang = ProcessInfo.processInfo.environment["LANG_KEY"] // "swift"
let cell = ProcessInfo.processInfo.environment["CELL"]
// parse game_state.json, apply move, write back
// full impl in implementations/swift/game.swift
```

</details>

---

## Language × GitHub Actions Support

| Language | Runtime | Actions Setup |
|----------|---------|---------------|
| Python | 3.12 | `setup-python@v5` |
| JavaScript | Node 20 | `setup-node@v4` |
| TypeScript | Node 20 + ts-node | `setup-node@v4` |
| Go | 1.22 | `setup-go@v5` |
| Rust | stable | `dtolnay/rust-toolchain` |
| Java | Temurin 21 | `setup-java@v4` |
| Kotlin | JVM (via java) | `setup-java@v4` |
| PHP | 8.3 | `shivammathur/setup-php@v2` |
| Ruby | 3.3 | `ruby/setup-ruby@v1` |
| C# | .NET 8 | `setup-dotnet@v4` |
| C | gcc (pre-installed) | — |
| C++ | g++ (pre-installed) | — |
| Scala | 3.x | `setup-java@v4` |
| Swift | 5.10 | `swift-actions/setup-swift@v2` |

---

*Built with GitHub Actions. Each **___** opens a pre-filled issue — submitting it triggers the workflow.*
