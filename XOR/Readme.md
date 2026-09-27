# 🔒 XOR 🔓

## 1. ¿Qué es XOR?

***XOR*** (abreviatura de *eXclusive OR*) es una operación lógica a nivel de bits. En matemáticas y criptografía se representa con el símbolo **$\oplus$**, mientras que en la mayoría de lenguajes de programación (como Python, C o Java) se utiliza el operador **`^`**.

La regla fundamental de XOR es muy sencilla: compara dos bits y devuelve `1` si los bits son ***diferentes***, y `0` si los bits son ***iguales***.

### Tabla de verdad

| Bit A | Bit B | A $\oplus$ B |
|:---:|:---:|:---:|
| 0 | 0 | **0** |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | **0** |

Debemos pensar en ***XOR*** como un interruptor condicional: el Bit B decide si el Bit A cambia o se queda igual (o viceversa). Si B es 1, A se invierte. Si B es 0, A se mantiene.

## Por qué usamos XOR en Criptografía?

XOR no es solo una operación lógica, posee unas propiedades algebraicas que lo convierten en el mecanismo perfecto para cifrar y descifrar información. 

Las propiedades fundamentales son:

1. **Elemento neutro:** $A \oplus 0 = A$ (Hacer XOR con 0 no cambia nada).
2. **Auto-inversa:** $A \oplus A = 0$ (Hacer XOR de algo consigo mismo lo anula).
3. **Conmutativa:** $A \oplus B = B \oplus A$ (El orden no importa).

### Cifrado y Descifrado Simétrico

Gracias a la propiedad **auto-inversa**, la misma operación y la misma clave sirven tanto para cifrar como para descifrar. Este es el principio básico de la criptografía simétrica.

* **Cifrado:** Texto Plano ($P$) $\oplus$ Clave ($K$) = Texto Cifrado ($C$)
* **Descifrado:** Texto Cifrado ($C$) $\oplus$ Clave ($K$) = Texto Plano ($P$)

**Demostración matemática:**
Si aplicamos la clave al texto cifrado, lo que estamos haciendo en realidad es esto:

$$C \oplus K = (P \oplus K) \oplus K = P \oplus (K \oplus K) = P \oplus 0 = P$$

Al aplicar XOR con la misma clave dos veces, la clave se "cancela" a sí misma y nos devuelve el mensaje original intacto. No necesitamos algoritmos complejos de ida y vuelta; XOR es su propio espejo.

#### CIFRADO: Ejemplo práctico

Imaginemos que tenemos el mensaje `HOLA` (en mayúsculas), y queremos cifrarlo usando la clave `B*:q` a través de XOR. Para ello:

##### [1.] Transformamos cada carácter del mensaje en su forma binaria (byte):

| Carácter ASCII | Código ASCII | Binario |
| :---: | :---: | :---: |
| *H* | 72 | `01001000` |
| *O* | 79 | `01001111` |
| *L* | 76 | `01001100` |
| *A* | 65 | `01000001` |

##### [2.] Transformamos cada carácter del mensaje en su forma binaria (byte):

| Carácter ASCII | Código ASCII | Binario |
| :---: | :---: | :---: |
| *B* | 66 | `01000010` |
| _*_ | 42 | `00101010` |
| *:* | 58 | `00111010` |
| *q* | 113 | `01110001` |

###### [3.] Cifrado XOR

Una vez que tenemos los caracteres en su forma binaria, debemos comparar las posiciones correspondientes del mensaje y la clave:

```text
'H' -> 01001000
'B' -> 01000010
       --------
       00001010 -> 10 -> "LF" (\n)

=======================================

'O' -> 01001111
'*' -> 00101010
       --------
       01100101 -> 101 -> (e)

=======================================          ---------> Mensaje cifrado -> "\nev0"

'L' -> 01001100
':' -> 00111010
       --------
       01110110 -> 118 -> (v)

=======================================

'A' -> 01000001
'q' -> 01110001
       --------
       00110000 -> 48 -> (0)
```

>[!important]
>Cuando hacemos XOR de dos letras legibles en ASCII, el resultado matemático suele caer en el rango de los ***caracteres de control*** (del `0x00` al `0x1F` o del `0` al `31`) o en caracteres extendidos. Si intentamos imprimir eso directamente en la terminal, veremos símbolos raros, la terminal hará cosas extrañas (como borrar líneas) o directamente no imprimirá nada.
>
>###### Qué podemos hacer con ellos?
>En criptografía, el texto cifrado nunca se trata como texto puro (*String*), sino como datos binarios crudos (*Bytes* o *Arrays de bytes*). Para poder mostrar ese resultado en pantalla, guardarlo en un archivo o enviarlo por internet sin que se rompa, lo que hacemos es ***codificarlo***.
>
>Las dos formas estándar de manejar (y mostrar) ese resultado XOR son:
>1. ***Hexadecimal (HEX):*** Representa cada dos caracteres legibles (del `0` al `9` y de la `a` a la `f`). Es lo más común en análisis de bajo nivel.
>2. ***Base64:*** Transforma los bytes binarios en un alfabeto seguro de 64 caracteres (letras, números, `+` y `/`).

Con todo esto, podemos representar el mensaje cifrado  de varias formas:

1. ***Texto Crudo (Raw Text):*** Mostramos el resultado con sus correspondientes caracteres ASCII siempre que sea posible (Es la menos aconsejable). Un ejemplo sería usar `repr()` en Python:
   ```text
   '\nev0'
   ```
2. ***Hexadecimal (HEX):*** Mostramos el resultado en hexadecimal:
   ```text
   0x0a657630
   ```
3. ***Base64:*** Lo codificamos para que pueda compartirse de forma más cómoda a través de internet:
   ```text
   CmV2MA==
   ```












