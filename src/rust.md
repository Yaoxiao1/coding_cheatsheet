# Rust

### 字符转 ACSII

```rust
let c : char = from_u32(49).unwrap();
let num : u32 = c as u32;
```

### 快速构建重复字符的字符串

```rust
let s : String = "abc".repeat(4) //"abcabcabcabc"
let s2 : String = "a".repeat(3) //"aaa"
```

### hashmap 判断是否存在，不存在就插入

```rust
use std::collections::HashMap;
HashMap.entry("").or_insert()
```

### hashmap 使用[(K,V);N]快速初始化

```rust
use std::collections::HashMap;
let map1 = HashMap::from([(1, 2), (3, 4)]);
let map2: HashMap<_, _> = [(1, 2), (3, 4)].into();
assert_eq!(map1, map2);
```
