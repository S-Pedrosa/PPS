# Actividade 1
A linguaxe de programación Python, desenvolvemento de código e tests unitarios

Contexto práctico #
Julián cuando necesita comprobar parte de un código en Python usa la librería incluida por defecto en las distribuciones de Python llamada unittest.

Tiene un pequeño programa llamado fibo.py que escribe la serie de Fibonacci hasta un número dado y devuelve el valor de esa misma posición.

Decide hacer un test del software de tipo aceptación. Es decir, quiere verificar que una parte del código se comporta de forma esperada. Para ello crea un script que importará la librería unittest y comprobará si el quinto número de la serie Fibonacci, el número 3, es correcto (la serie Fibonacci es 0,1,1,2,3,5,8,13…).

Para ello, importa la librería de test de software unittest y define una clase donde incluiría la función para comprobar esta parte especifica del código. Va a comprobar que el quinto número de la serie sea igual a 3, lo hace mediante la sentencia self.assertEqual(result, 3).

¿Qué se pide? #
Antes de nada reflejaremos la sucesión de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34… Tienes mas información sobre esta interesante sucesión y su origen aquí

Crea un script que genere la secuencia de Fibonacci
Puedes usar cualquier lenguaje con el que estés familiarizado, pero te recomiendo por facilidad y por el gran acceso a librerías de evaluación de software el lenguaje Python. Si aún no has programado en Python, su inmersión te será sencilla y amigable.

Llamaremos a este script fibo.py (en el caso en que estemos programando en python)

Deberías de crear un programa con su estructura completa. Dentro de este programa, crearemos una funciona llamada fibonacci.

Creación del programa principal
2.1. Crearemos un programa principal donde definiremos una clase llamada Test, desde donde probaremos nuestro software.

2.2. Importaremos la librería de testeo de software, en este caso unittest de Python.

2.3. Crearemos nuestra clase (del tipo unittest.TestCase)

2.4. Dentro de esta clase definiremos una función (podemos llamarla como consideremos, pero es recomendable un nombre ilustrativo)

Dentro de la función reflejaremos el tipo de testeo que vamos a realizar. En este caso nuestro objetivo es verificar si la posición X de la sucesión de Fibonacci coincide con el resultado esperado. Es decir, si coincide con la posición X que devuelve nuestro programa. Para ello, comprobamos que el quinto número de la sucesión, que es 3, coincide con el quinto número que devuelve nuestra secuencia. Para hacer esta comprobación usaremos el tipo de comprobación assertequal, que comprueba si dos valores son iguales.

Mediante esta función comprobaremos si la posición quinta de nuestra función coincide con el valor esperado (el valor esperado es la quinta posición de la sucesión que es 3)

3: Verificación de software y pregunta final

Ejecutaremos el programa final y verificaremos si realmente nuestro programa que calcula la sucesión de Fibonacci (fibo.py) se comporta como esperamos. Si el programa que comprueba el código detecta un error, nos reflejará que dato está esperando y que ha recibido. ¿Qué tipo de prueba hemos realizado?
