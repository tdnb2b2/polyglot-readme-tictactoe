# 🎮 Polyglot README Tic-Tac-Toe

> **Tic-Tac-Toe playable directly on this README — in 14 programming languages.**  
> Each language runs its own independent board, powered by GitHub Actions.  
> Click **[___]** to make a move. The corresponding language implementation processes your move and updates this README.

---

## How to Play

1. Pick a language board below
2. Click any **[___]** cell — it opens a pre-filled GitHub Issue
3. Submit the issue — GitHub Actions runs that language's implementation
4. The board updates automatically within ~30 seconds
5. Players alternate: ❌ goes first, then ⭕

**Move format:** `<Language>: Tic-Tac-Toe: Put <Cell>` (e.g. `Python: Tic-Tac-Toe: Put B2`)

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
import json, os

# Read the simplified state
with open('game_state.json', 'r') as f:
    all_states = json.load(f)
    s = all_states["python"]

cell   = os.environ.get('CELL', '').upper()
action = os.environ.get('ACTION', 'put')

if action == 'reset':
    s = {"board": [["","",""],["","",""],["","",""]], "turn": "X", "winner": None, "log": []}
elif cell and not s["winner"]:
    # Apply Tic-Tac-Toe logic...
    pass

# Write it back
all_states["python"] = s
with open('game_state.json', 'w') as f:
    json.dump(all_states, f, indent=2)
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
const all = JSON.parse(fs.readFileSync('game_state.json'));
const lang = process.env.LANG_KEY;
const cell = process.env.CELL;
const action = process.env.ACTION;
const s = all[lang];

if (action === 'reset') {
  s.board = [['','',''],['','',''],['','','']];
  s.turn = 'X'; s.winner = null; s.log = [];
} else {
  // Apply coordinate mapping and win check...
}
all[lang] = s;
fs.writeFileSync('game_state.json', JSON.stringify(all, null, 2));
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
const all = JSON.parse(fs.readFileSync('game_state.json','utf8'));
const lang = process.env.LANG_KEY!;
const s = all[lang];
// ... Tic-Tac-Toe logic ...
fs.writeFileSync('game_state.json', JSON.stringify(all,null,2));
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
import (
    "encoding/json"; "os"; "strings"
)
func main() {
    lang := os.Getenv("LANG_KEY") // "go"
    // parse game_state.json, apply move, write back
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
use std::{env, fs};
use serde_json::{Value, json};

fn main() {
    let lang = env::var("LANG_KEY").unwrap(); // "rust"
    // parse game_state.json, apply move, write back
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
import org.json.*;
import java.nio.file.*;

public class Game {
    public static void main(String[] args) throws Exception {
        String lang = System.getenv("LANG_KEY"); // "java"
        // parse game_state.json, apply move, write back
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
import org.json.JSONObject
import java.io.File

fun main() {
    val lang = System.getenv("LANG_KEY") // "kotlin"
    // parse game_state.json, apply move, write back
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
$all  = json_decode(file_get_contents('game_state.json'), true);
// apply move logic...
file_put_contents('game_state.json', json_encode($all, JSON_PRETTY_PRINT));
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
require 'json'
lang = ENV['LANG_KEY'] # "ruby"
all  = JSON.parse(File.read('game_state.json'))
# apply move logic...
File.write('game_state.json', JSON.pretty_generate(all))
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
using System.Text.Json;
var lang = Environment.GetEnvironmentVariable("LANG_KEY"); // "csharp"
// parse game_state.json, apply move, write back
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
// Uses cJSON for JSON parsing

int main() {
    const char* lang = getenv("LANG_KEY"); // "c"
    // parse game_state.json, apply move, write back
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
#include <fstream>
#include <nlohmann/json.hpp>

int main() {
    std::string lang = std::getenv("LANG_KEY"); // "cpp"
    // parse game_state.json...
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
import scala.io.Source
import play.api.libs.json._

object Game extends App {
    val lang = sys.env("LANG_KEY") // "scala"
    // parse game_state.json...
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

let lang = ProcessInfo.processInfo.environment["LANG_KEY"]! // "swift"
// parse game_state.json...
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
| Scala | 3.x via Coursier | `setup-java@v4` |
| Swift | 5.10 | `swift-actions/setup-swift@v2` |

---

*Built with GitHub Actions. Each **[___]** opens a pre-filled issue — submitting it triggers the workflow.*
