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

##### [2.] Transformamos cada carácter de la clave en su forma binaria (byte):

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

#### DESCIFRADO: Ejemplo práctico

Partiendo del mismo ejemplo anterior, vamos a descifrarlo usando exactamente el mismo método que al cifrar el mensaje:

##### [1.] Transformamos cada carácter del mensaje cifrado en su forma binaria (byte):

| Carácter ASCII | Código ASCII | Binario |
| :---: | :---: | :---: |
| *\n* | 10 | `00001010` |
| *e* | 101 | `01100101` |
| *v* | 118 | `01110110` |
| *0* | 48 | `00110000` |

##### [2.] Transformamos cada carácter de la clave en su forma binaria (byte):

| Carácter ASCII | Código ASCII | Binario |
| :---: | :---: | :---: |
| *B* | 66 | `01000010` |
| _*_ | 42 | `00101010` |
| *:* | 58 | `00111010` |
| *q* | 113 | `01110001` |

###### [3.] Cifrado XOR

Una vez que tenemos los caracteres en su forma binaria, debemos comparar las posiciones correspondientes del mensaje y la clave:

```text
'\n' -> 00001010
'B'  -> 01000010
        --------
        01001000 -> 72 -> (H)

=======================================

'e' -> 01100101
'*' -> 00101010
       --------
       01001111 -> 79 -> (o)

=======================================          ---------> Mensaje descifrado -> "HOLA"

'v' -> 01110110
':' -> 00111010
       --------
       01001100 -> 76 -> (L)

=======================================

'0' -> 00110000
'q' -> 01110001
       --------
       01000001 -> 65 -> (A)
```

>Vemos que siguiendo exactamente el mismo proceso de cifrado, podemos descifrar el mensaje siempre y cuando tengamos la clave de cifrado.

#### Cifrado y Descifrado con mensajes y claves diferentes

Hasta ahora, ambos ejemplos que hemos puesto han tenido la misma longitud tanto el mensaje como la clave de cifrado. Y aunque es lo recomendable, no tiene porque ser así. Podemos cifrar y descifrar mensajes que son más largos (o cortos, lo cual no tiene demasiado sentido) que la clave de cifrado:

##### Cifrado: `len(Mensaje)` > `len(clave)`

>En esta ocasión, usaremos la clave `Hola Don PePIto` con la clave `kik2@1`

| Carácter ASCII | Código ASCII | Binario |
| :---: | :---: | :---: |
| *H* | 72 | `01001000` |
| *o* | 111 | `01101111` |
| *l* | 108 | `01101100` |
| *a* | 97 | `01100001` |
| *' '* | 32 | `00100000` |
| *D* | 68 | `01000100` |
| *o* | 111 | `01101111` |
| *n* | 110 | `01101110` |
| *' '* | 32 | `00100000` |
| *P* | 80 | `01010000` |
| *e* | 101 | `01100101` |
| *P* | 80 | `01010000` |
| *I* | 73 | `01001001` |
| *t* | 116 | `01110100` |
| *o* | 111 | `01101111` |

```Python
print(len("Hola Don PePIto"))  # 15 caracteres
```

| Carácter ASCII | Código ASCII | Binario |
| :---: | :---: | :---: |
| *k* | 107 | `01101011` |
| _i_ | 106 | `01101010` |
| *k* | 107 | `01101011` |
| *2* | 50 | `00110010` |
| *@* | 64 | `01000000` |
| *1* | 49 | `00110001` |

```Python
print(len("kik2@1"))  # 6 caracteres
```

>Obviamente, el mensaje a cifrar es mucho más largo que la clave de cifrado. Esto es un problema de seguridad, pero no nos impide cifrar el mensaje.

Para cifrar el mensaje con una clave más corta, tan solo debemos de ir repitiendo los caracteres correspondientes de la clave hasta que cifremos todos los caracteres del mensaje:

```text
"Hola Don PePIto": 01001000 01101111 01101100 01100001 00100000 01000100 01101111 01101110 00100000 01010000 01100101 01010000 01001001 01110100 01101111
"kik2@1":          01101011 01101001 01101011 00110010 01000000 00110001 01101011 01101001 01101011 00110010 01000000 00110001 01101011 01101001 01101011
                       k        i        k        2        @        1   |    k        i        k        2        @        1   |    k        i        k
                   --------------------------------------------------------------------------------------------------------------------------------------
                   00100011 00000110 00000111 01010011 01100000 01110101 00000100 00000111 01001011 01100010 00100101 01100001 00100010 00011101 00000100

Resultado -> '#\x06\x07S`u\x04\x07Kb%a"\x1d\x04'
```

>En el ejemplo anterior podemos ver un mensaje cifrado con una clave mucho menor que él.

##### Por qué es una mala práctica?

Usar una clave más corta que el mensaje obliga a repetir la clave cíclicamente para cubrir toda la longitud del texto. En criptografía, esta repetición destruye la seguridad matemática del cifrado, convirtiendo un mensaje supuestamente ilegible en un rompecabezas estadístico trivial de resolver.

Aunque es útil para ofuscar payloads rápidos contra antivirus básicos, es criptográficamente débil por tres motivos fundamentales:

##### 1. Fuga de patrones y Análisis de Frecuencias
El lenguaje humano y los lenguajes de programación (HTML, Bash, Python) no son aleatorios; tienen estructuras repetitivas (espacios, vocales comunes, etiquetas como `<div>` o comandos como `echo`).

Si nuestra clave se repite cada 5 bytes y la palabra "admin" aparece varias veces en el texto original, es muy probable que esas letras se alineen con los mismos caracteres de la clave en más de una ocasión. Esto genera secuencias idénticas en el texto cifrado. Un atacante puede usar técnicas como el *Método Kasiski* para medir la distancia entre estos bloques repetidos y deducir exactamente la longitud de la clave. Una vez conoce la longitud, puede aplicar análisis de frecuencias estándar para romper el cifrado en segundos.

##### 2. Vulnerabilidad extrema al "Known-Plaintext Attack" (KPA)
En la propiedad matemática del XOR, si `Texto ^ Clave = Cifrado`, entonces `Cifrado ^ Texto = Clave`.

Si un atacante intercepta nuestro mensaje y puede adivinar tan solo un pequeño fragmento de lo que contiene (por ejemplo, sabe que el mensaje empieza por `HTTP/1.1` o que contiene `#!/bin/bash`), puede aplicar XOR entre ese fragmento adivinado y nuestro texto cifrado.

Si la clave era igual de larga que el mensaje, el atacante solo descubre esos 10 bytes aislados de la clave y el resto sigue seguro.

Si la clave era corta y se repetía, al descubrir 10 bytes acaba de revelar la clave entera. Solo tiene que coger ese fragmento, volver a aplicarlo en bucle sobre todo el mensaje, y descifrar el 100% de la comunicación.

##### 3. La técnica del "Crib Dragging"
Incluso si el atacante no sabe exactamente en qué parte del texto está la palabra adivinada (llamada *crib*), puede usar un script para arrastrar esa palabra byte a byte por todo el texto cifrado. Como la clave es corta y se repite, en el momento en que el crib se alinea correctamente, el texto resultante mostrará letras de la clave repetida de forma evidente, delatando su posición.

##### La Regla de Oro: El Cifrado de Libreta de un Solo Uso (One-Time Pad)
Para que un cifrado (como el XOR) sea matemáticamente irrompible, debe cumplir tres leyes estrictas:

- La clave debe ser generada de forma verdaderamente aleatoria.

- La clave nunca debe reutilizarse.

- La clave debe ser al menos tan larga como el mensaje.

Si se cumplen estas tres reglas, el cifrado adquiere "*Secreto Perfecto*". El atacante podría probar todas las claves posibles por fuerza bruta y obtendría todos los mensajes posibles del universo que encajen en esa longitud, sin ninguna pista matemática que le indique cuál es el mensaje real. Reducir la clave y repetirla rompe esta premisa al instante.
