# Reference Guide for 8sc Assembly
*Note: Instruction memory and data memory are separate. Instruction memory is read only, data memory is read/write. `Ld` and `str` read from data memory.*
## Instructions

### General Instruction Format

All instructions words are 8 bits. Within these 8 bits, the first 3 represent the command to be exectuted. The remaining 5 bits are parameters for that instruction.

The remaining 5 bits may contain differing amounts of the four following parameters:
`reg`,`restrictreg`, `constant`, and `direction`

Additionally, there may be a single zero bit at the end for padding: `zero`

### Parameter Definition 

#### Reg

Reg represents either register A, B, C, or D. 

##### Bit representation

- A = 00

- B = 01

- C = 10

- D = 11


##### Assembly representation

- A = "a"

- B = "b"

- C = "c"

- D = "d"

#### Restrictreg

Reg represents either register A, B, C, or D. 

##### Bit representation

- A = 0

- B = 1


##### Assembly representation

- A = "a"

- B = "b"

#### Direction

Reg represents either the positive direction or the negative direction. 

##### Bit representation

- \+ = 0

- \- = 1


##### Assembly representation

- \+ = "+"

- \- = "-"


#### Constant

Constant can be any valid decimal number between 0 \(inclusive\) and 15 \(inclusive).

##### Bit representation

Constant is represented as a 4 bit unsigned number.

##### Assembly representation

"1", "2", "3", ..., "14", "15"

### Specfic Instruction Format

#### Add

First 3 bits - `000`

Last 5 bits - `reg` `reg` `zero`

##### Function

The first register is set to the addition of the first and second register.


##### Example assembly

`add a d`

#### Nand

First 3 bits - `001`

Last 5 bits - `reg` `reg` `zero`

##### Function

The first register is set to the bitwise nanding of the first and second register.

##### Example assembly

`nand b c`


#### Shftrt

First 3 bits - `010`

Last 5 bits - `reg` `reg` `zero`

##### Function

The first register is set to the first register shifted right by the amount in the second register.

##### Example assembly

`shftrt c c`

#### Bgt

First 3 bits - `011`

Last 5 bits - `direction` `constant`

##### Example assembly

`bgt - 14`

##### Function

If an addition, nanding, or shift right was performed in the last instruction and the first register was greater than the second register in that instruction, then the pc counter jumps in the direction and amount specified.


#### Ld

First 3 bits - `100`

Last 5 bits - `reg` `reg` `zero`

##### Function

The first register is set to the value of the data memory at the index specified by the second register.

##### Example assembly

`ld a d`

#### Str

First 3 bits - `101`

Last 5 bits - `reg` `reg` `zero`

##### Function

The value of the first register is stored in data memory at the index specified by the second register.

##### Example assembly

`str c d`

#### Ldl

First 3 bits - `110`

Last 5 bits - `restrictedreg` `constant`

##### Function

The lower 4 bits of the specified register is set to the value of the constant.

##### Example assembly

`ldl a 15`

#### Ldh

First 3 bits - `111`

Last 5 bits - `restrictedreg` `constant`

##### Function

The upper 4 bits of the specified register is set to the value of the constant.

##### Example assembly

`ldh b 1`

## Instruction Addresses

All instructions must be prepended by the address that they are placed at. Please note that this is in decimal and can be any value from 000 to 255.

Example code with addressing:
```
# a is the current address, b is the constant to store, c is the amount to increment the address by
000 ldh a 0
001 ldl a 1
002 ldh b 10
003 ldl b 10
004 add c a # This stores 1 in c
005 ldh a 15 
006 ldl a 15
007 add d a # This stores 255 in d
008 ldh a 0
009 ldl a 0
010 str b a
011 add a c
012 nand d c
013 bgt - 3

```

## BNF Definition of Assembly Language

[BNF Playground link](https://bnfplayground.pauliankline.com/?bnf=%3Clines%3E%20%3A%3A%3D%20%3Cline%3E%20%7C%20%3Clines%3E%20%3Cline%3E%0A%3Cline%3E%20%3A%3A%3D%20%3Caddress%3E%20%22%20%22%20%3Ccommand%3E%0A%3Ccommand%3E%20%3A%3A%3D%20%3Cadd%3E%20%22%5Cn%22%20%7C%20%3Cnand%3E%20%22%5Cn%22%20%7C%20%3Cshftrt%3E%20%22%5Cn%22%20%7C%0A%3Cbgt%3E%20%22%5Cn%22%20%7C%20%3Cld%3E%20%22%5Cn%22%20%7C%20%3Cstr%3E%20%22%5Cn%22%20%7C%20%3Cldl%3E%20%22%5Cn%22%20%7C%20%3Cldh%3E%20%22%5Cn%22%0A%0A%3Cadd%3E%20%3A%3A%3D%20%22add%22%20%22%20%22%20%3Cregister%3E%20%22%20%22%20%3Cregister%3E%0A%3Cnand%3E%20%3A%3A%3D%20%22nand%22%20%22%20%22%20%3Cregister%3E%20%22%20%22%20%3Cregister%3E%0A%3Cshftrt%3E%20%3A%3A%3D%20%22shftrt%22%20%22%20%22%20%3Cregister%3E%20%22%20%22%20%3Cregister%3E%0A%3Cbgt%3E%20%3A%3A%3D%20%22bgt%22%20%22%20%22%20%3Cdirection%3E%20%22%20%22%20%3Cconstant%3E%0A%3Cld%3E%20%3A%3A%3D%20%22ld%22%20%22%20%22%20%3Cregister%3E%20%22%20%22%20%3Cregister%3E%0A%3Cstr%3E%20%3A%3A%3D%20%22str%22%20%22%20%22%20%3Cregister%3E%20%22%20%22%20%3Cregister%3E%0A%3Cldl%3E%20%3A%3A%3D%20%22ldl%22%20%22%20%22%20%3Crestricted_registers%3E%20%22%20%22%20%3Cconstant%3E%0A%3Cldh%3E%20%3A%3A%3D%20%22ldh%22%20%22%20%22%20%3Crestricted_registers%3E%20%22%20%22%20%3Cconstant%3E%0A%0A%0A%3Cdirection%3E%20%3A%3A%3D%20%22-%22%20%7C%20%22%2B%22%0A%3Cconstant%3E%20%3A%3A%3D%20%220%22%20%7C%20%221%22%20%7C%20%222%22%20%7C%20%223%22%20%7C%20%224%22%20%7C%20%225%22%20%7C%20%226%22%20%7C%20%227%22%20%7C%20%228%22%20%7C%20%229%22%20%7C%20%2210%22%20%7C%20%2211%22%20%7C%20%2212%22%20%7C%20%2213%22%20%7C%20%2214%22%20%7C%20%2215%22%0A%3Cregister%3E%20%3A%3A%3D%20%3Crestricted_registers%3E%20%7C%20%22c%22%20%7C%20%22d%22%0A%3Crestricted_registers%3E%20%3A%3A%3D%20%22a%22%20%7C%20%22b%22%0A%0A%3Caddress%3E%20%3A%3A%3D%20%22000%22%20%7C%20%22001%22%20%7C%20%22002%22%20%7C%20%22003%22%20%7C%20%22004%22%20%7C%20%22005%22%20%7C%20%22006%22%20%7C%20%22007%22%20%7C%20%22008%22%20%7C%20%22009%22%20%7C%20%0A%22010%22%20%7C%20%22011%22%20%7C%20%22012%22%20%7C%20%22013%22%20%7C%20%22014%22%20%7C%20%22015%22%20%7C%20%22016%22%20%7C%20%22017%22%20%7C%20%22018%22%20%7C%20%22019%22%20%7C%20%0A%22020%22%20%7C%20%22021%22%20%7C%20%22022%22%20%7C%20%22023%22%20%7C%20%22024%22%20%7C%20%22025%22%20%7C%20%22026%22%20%7C%20%22027%22%20%7C%20%22028%22%20%7C%20%22029%22%20%7C%20%0A%22030%22%20%7C%20%22031%22%20%7C%20%22032%22%20%7C%20%22033%22%20%7C%20%22034%22%20%7C%20%22035%22%20%7C%20%22036%22%20%7C%20%22037%22%20%7C%20%22038%22%20%7C%20%22039%22%20%7C%20%0A%22040%22%20%7C%20%22041%22%20%7C%20%22042%22%20%7C%20%22043%22%20%7C%20%22044%22%20%7C%20%22045%22%20%7C%20%22046%22%20%7C%20%22047%22%20%7C%20%22048%22%20%7C%20%22049%22%20%7C%20%0A%22050%22%20%7C%20%22051%22%20%7C%20%22052%22%20%7C%20%22053%22%20%7C%20%22054%22%20%7C%20%22055%22%20%7C%20%22056%22%20%7C%20%22057%22%20%7C%20%22058%22%20%7C%20%22059%22%20%7C%20%0A%22060%22%20%7C%20%22061%22%20%7C%20%22062%22%20%7C%20%22063%22%20%7C%20%22064%22%20%7C%20%22065%22%20%7C%20%22066%22%20%7C%20%22067%22%20%7C%20%22068%22%20%7C%20%22069%22%20%7C%20%0A%22070%22%20%7C%20%22071%22%20%7C%20%22072%22%20%7C%20%22073%22%20%7C%20%22074%22%20%7C%20%22075%22%20%7C%20%22076%22%20%7C%20%22077%22%20%7C%20%22078%22%20%7C%20%22079%22%20%7C%20%0A%22080%22%20%7C%20%22081%22%20%7C%20%22082%22%20%7C%20%22083%22%20%7C%20%22084%22%20%7C%20%22085%22%20%7C%20%22086%22%20%7C%20%22087%22%20%7C%20%22088%22%20%7C%20%22089%22%20%7C%20%0A%22090%22%20%7C%20%22091%22%20%7C%20%22092%22%20%7C%20%22093%22%20%7C%20%22094%22%20%7C%20%22095%22%20%7C%20%22096%22%20%7C%20%22097%22%20%7C%20%22098%22%20%7C%20%22099%22%20%7C%20%0A%22100%22%20%7C%20%22101%22%20%7C%20%22102%22%20%7C%20%22103%22%20%7C%20%22104%22%20%7C%20%22105%22%20%7C%20%22106%22%20%7C%20%22107%22%20%7C%20%22108%22%20%7C%20%22109%22%20%7C%20%0A%22110%22%20%7C%20%22111%22%20%7C%20%22112%22%20%7C%20%22113%22%20%7C%20%22114%22%20%7C%20%22115%22%20%7C%20%22116%22%20%7C%20%22117%22%20%7C%20%22118%22%20%7C%20%22119%22%20%7C%20%0A%22120%22%20%7C%20%22121%22%20%7C%20%22122%22%20%7C%20%22123%22%20%7C%20%22124%22%20%7C%20%22125%22%20%7C%20%22126%22%20%7C%20%22127%22%20%7C%20%22128%22%20%7C%20%22129%22%20%7C%20%0A%22130%22%20%7C%20%22131%22%20%7C%20%22132%22%20%7C%20%22133%22%20%7C%20%22134%22%20%7C%20%22135%22%20%7C%20%22136%22%20%7C%20%22137%22%20%7C%20%22138%22%20%7C%20%22139%22%20%7C%20%0A%22140%22%20%7C%20%22141%22%20%7C%20%22142%22%20%7C%20%22143%22%20%7C%20%22144%22%20%7C%20%22145%22%20%7C%20%22146%22%20%7C%20%22147%22%20%7C%20%22148%22%20%7C%20%22149%22%20%7C%20%0A%22150%22%20%7C%20%22151%22%20%7C%20%22152%22%20%7C%20%22153%22%20%7C%20%22154%22%20%7C%20%22155%22%20%7C%20%22156%22%20%7C%20%22157%22%20%7C%20%22158%22%20%7C%20%22159%22%20%7C%20%0A%22160%22%20%7C%20%22161%22%20%7C%20%22162%22%20%7C%20%22163%22%20%7C%20%22164%22%20%7C%20%22165%22%20%7C%20%22166%22%20%7C%20%22167%22%20%7C%20%22168%22%20%7C%20%22169%22%20%7C%20%0A%22170%22%20%7C%20%22171%22%20%7C%20%22172%22%20%7C%20%22173%22%20%7C%20%22174%22%20%7C%20%22175%22%20%7C%20%22176%22%20%7C%20%22177%22%20%7C%20%22178%22%20%7C%20%22179%22%20%7C%20%0A%22180%22%20%7C%20%22181%22%20%7C%20%22182%22%20%7C%20%22183%22%20%7C%20%22184%22%20%7C%20%22185%22%20%7C%20%22186%22%20%7C%20%22187%22%20%7C%20%22188%22%20%7C%20%22189%22%20%7C%20%0A%22190%22%20%7C%20%22191%22%20%7C%20%22192%22%20%7C%20%22193%22%20%7C%20%22194%22%20%7C%20%22195%22%20%7C%20%22196%22%20%7C%20%22197%22%20%7C%20%22198%22%20%7C%20%22199%22%20%7C%20%0A%22200%22%20%7C%20%22201%22%20%7C%20%22202%22%20%7C%20%22203%22%20%7C%20%22204%22%20%7C%20%22205%22%20%7C%20%22206%22%20%7C%20%22207%22%20%7C%20%22208%22%20%7C%20%22209%22%20%7C%20%0A%22210%22%20%7C%20%22211%22%20%7C%20%22212%22%20%7C%20%22213%22%20%7C%20%22214%22%20%7C%20%22215%22%20%7C%20%22216%22%20%7C%20%22217%22%20%7C%20%22218%22%20%7C%20%22219%22%20%7C%20%0A%22220%22%20%7C%20%22221%22%20%7C%20%22222%22%20%7C%20%22223%22%20%7C%20%22224%22%20%7C%20%22225%22%20%7C%20%22226%22%20%7C%20%22227%22%20%7C%20%22228%22%20%7C%20%22229%22%20%7C%20%0A%22230%22%20%7C%20%22231%22%20%7C%20%22232%22%20%7C%20%22233%22%20%7C%20%22234%22%20%7C%20%22235%22%20%7C%20%22236%22%20%7C%20%22237%22%20%7C%20%22238%22%20%7C%20%22239%22%20%7C%20%0A%22240%22%20%7C%20%22241%22%20%7C%20%22242%22%20%7C%20%22243%22%20%7C%20%22244%22%20%7C%20%22245%22%20%7C%20%22246%22%20%7C%20%22247%22%20%7C%20%22248%22%20%7C%20%22249%22%20%7C%20%0A%22250%22%20%7C%20%22251%22%20%7C%20%22252%22%20%7C%20%22253%22%20%7C%20%22254%22%20%7C%20%22255%22%20%7C%20%22256%22&name=)

```bnf
<lines> ::= <line> | <lines> <line>
<line> ::= <address> " " <command>
<command> ::= <add> "\n" | <nand> "\n" | <shftrt> "\n" |
<bgt> "\n" | <ld> "\n" | <str> "\n" | <ldl> "\n" | <ldh> "\n"

<add> ::= "add" " " <register> " " <register>
<nand> ::= "nand" " " <register> " " <register>
<shftrt> ::= "shftrt" " " <register> " " <register>
<bgt> ::= "bgt" " " <direction> " " <constant>
<ld> ::= "ld" " " <register> " " <register>
<str> ::= "str" " " <register> " " <register>
<ldl> ::= "ldl" " " <restricted_registers> " " <constant>
<ldh> ::= "ldh" " " <restricted_registers> " " <constant>


<direction> ::= "-" | "+"
<constant> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11" | "12" | "13" | "14" | "15"
<register> ::= <restricted_registers> | "c" | "d"
<restricted_registers> ::= "a" | "b"

<address> ::= "000" | "001" | "002" | "003" | "004" | "005" | "006" | "007" | "008" | "009" | 
"010" | "011" | "012" | "013" | "014" | "015" | "016" | "017" | "018" | "019" | 
"020" | "021" | "022" | "023" | "024" | "025" | "026" | "027" | "028" | "029" | 
"030" | "031" | "032" | "033" | "034" | "035" | "036" | "037" | "038" | "039" | 
"040" | "041" | "042" | "043" | "044" | "045" | "046" | "047" | "048" | "049" | 
"050" | "051" | "052" | "053" | "054" | "055" | "056" | "057" | "058" | "059" | 
"060" | "061" | "062" | "063" | "064" | "065" | "066" | "067" | "068" | "069" | 
"070" | "071" | "072" | "073" | "074" | "075" | "076" | "077" | "078" | "079" | 
"080" | "081" | "082" | "083" | "084" | "085" | "086" | "087" | "088" | "089" | 
"090" | "091" | "092" | "093" | "094" | "095" | "096" | "097" | "098" | "099" | 
"100" | "101" | "102" | "103" | "104" | "105" | "106" | "107" | "108" | "109" | 
"110" | "111" | "112" | "113" | "114" | "115" | "116" | "117" | "118" | "119" | 
"120" | "121" | "122" | "123" | "124" | "125" | "126" | "127" | "128" | "129" | 
"130" | "131" | "132" | "133" | "134" | "135" | "136" | "137" | "138" | "139" | 
"140" | "141" | "142" | "143" | "144" | "145" | "146" | "147" | "148" | "149" | 
"150" | "151" | "152" | "153" | "154" | "155" | "156" | "157" | "158" | "159" | 
"160" | "161" | "162" | "163" | "164" | "165" | "166" | "167" | "168" | "169" | 
"170" | "171" | "172" | "173" | "174" | "175" | "176" | "177" | "178" | "179" | 
"180" | "181" | "182" | "183" | "184" | "185" | "186" | "187" | "188" | "189" | 
"190" | "191" | "192" | "193" | "194" | "195" | "196" | "197" | "198" | "199" | 
"200" | "201" | "202" | "203" | "204" | "205" | "206" | "207" | "208" | "209" | 
"210" | "211" | "212" | "213" | "214" | "215" | "216" | "217" | "218" | "219" | 
"220" | "221" | "222" | "223" | "224" | "225" | "226" | "227" | "228" | "229" | 
"230" | "231" | "232" | "233" | "234" | "235" | "236" | "237" | "238" | "239" | 
"240" | "241" | "242" | "243" | "244" | "245" | "246" | "247" | "248" | "249" | 
"250" | "251" | "252" | "253" | "254" | "255" | "256"
```
