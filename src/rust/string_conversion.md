## Prelude
``` rust
use std::str;
```

### From Vec<char>
``` rust
fn main() {
    let src: Vec<char> = vec!['j','{','"','i','m','m','y','"','}'];
    // to String
    let string1: String = src.iter().collect::<String>();
    // to str
    let str1: &str = &src.iter().collect::<String>();
    // to vec of byte
    let byte1: Vec<u8> = src.iter().map(|c| *c as u8).collect::<Vec<_>>();
    println!("Vec<char>:{:?} \nString:{:?}\nstr:{:?}\nVec<u8>:{:?}", src, string1, str1, byte1);
}
```


### From Vec<u8>
``` rust
fn main() {
    // in rust, this is a slice
    // b - byte, r - raw string, br - byte of raw string
    let src: Vec<u8> = br#"e{"ddie"}"#.to_vec();
    // to String
    // from_utf8 consume the vector of bytes
    let string2: String = String::from_utf8(src.clone()).unwrap();
    // to str
    let str2: &str = str::from_utf8(&src).unwrap();
    // to vec of chars
    let char2: Vec<char> = src.iter().map(|b| *b as char).collect::<Vec<_>>();
    println!("Vec<u8>:{:?} \nString:{:?}\nstr:{:?}\nVec<char>:{:?}", src, string2, str2, char2);
}
```


### From String
``` rust
fn main() {
    let src: String = String::from(r#"o{"livia"}"#);
    let str3: &str = &src;
    let char3: Vec<char> = src.chars().collect::<Vec<_>>();
    let byte3: Vec<u8> = src.as_bytes().to_vec();
    println!("String:{:?} \nstr:{:?}\nVec<char>:{:?}\nVec<u8>:{:?}", src, str3, char3, byte3);
}
```


### From str
``` rust
fn main() {
    let src: &str = r#"g{'race'}"#;
    let string4 = String::from(src);
    let char4: Vec<char> = src.chars().collect();
    let byte4: Vec<u8> = src.as_bytes().to_vec();
    println!("str:{:?} \nString:{:?}\nVec<char>:{:?}\nVec<u8>:{:?}", src, string4, char4, byte4);
}
```