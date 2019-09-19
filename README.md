##Modelo de Ising-Gauber

El modelo de Ising es probablemente el modelo más estudiado en mecánica estadística, en gran medida por su simplicidad y su utilidad en la comprensión de las transiciones de fase así como también por su gran rango de aplicación. En el modelo clásico de Ising, espines que existen en sitios de la red regular tienen dos posibles valores <img src="/tex/ac79f544ac468d9cd8eb78cb27613b1a.svg?invert_in_darkmode&sanitize=true" align=middle width=50.62775354999999pt height=21.18721440000001pt/>. El Hamiltoniano del sistema es el siguiente:

<p align="center"><img src="/tex/358dd85fd2862f07123c3d712fb653e1.svg?invert_in_darkmode&sanitize=true" align=middle width=409.6307754pt height=40.548151049999994pt/></p>

Donde la suma es sobre todos los pares de primeros vecinos. Así todo par paralelo de espines aporta al sistema  una energía <img src="/tex/81034b6c32f9c5d7adb1506259fa37c8.svg?invert_in_darkmode&sanitize=true" align=middle width=23.48178689999999pt height=22.465723500000017pt/> y los antiparalelos aportan <img src="/tex/8eb543f68dac24748e65e2e4c5fc968c.svg?invert_in_darkmode&sanitize=true" align=middle width=10.69635434999999pt height=22.465723500000017pt/>. Todas las propiedades de equilibrio del sistema pueden ser obtenidas a partir de la función de partición <img src="/tex/9398f7be2715f5f7d656029cd5bf0fc0.svg?invert_in_darkmode&sanitize=true" align=middle width=92.02568429999998pt height=27.91243950000002pt/>, donde la suma es sobre todas las configuraciones de espines en el sistema, y <img src="/tex/979db2d6ece9284957fc4d99ee71496e.svg?invert_in_darkmode&sanitize=true" align=middle width=80.28328604999999pt height=24.65753399999998pt/> es el inverso de la temperatura. Para <img src="/tex/0b5b3b3bb6d2c0b9dcc5b75bc8334b07.svg?invert_in_darkmode&sanitize=true" align=middle width=40.83319019999999pt height=22.465723500000017pt/>, aparece el ferromágnetismo de forma espontánea por debajo de la temperatura crítica <img src="/tex/f3087bed09ac6d957af8ecfe91212479.svg?invert_in_darkmode&sanitize=true" align=middle width=15.480837899999988pt height=22.465723500000017pt/> en dimensiones superiores a <img src="/tex/4cfe92e893a7541f68473ecb08419237.svg?invert_in_darkmode&sanitize=true" align=middle width=38.69280359999998pt height=22.831056599999986pt/> y campo externo nulo. En ese estado la magnetización es diferente de cero y espines distantes estan correlacionados. Sin embargo, por encima de la temperatura crítica <img src="/tex/f3087bed09ac6d957af8ecfe91212479.svg?invert_in_darkmode&sanitize=true" align=middle width=15.480837899999988pt height=22.465723500000017pt/> los espines estan distribuidos de tal forma que existen igual cantidad de espines con <img src="/tex/776f93672423b6ad1b8808ea2f124452.svg?invert_in_darkmode&sanitize=true" align=middle width=37.84231934999999pt height=21.18721440000001pt/> y <img src="/tex/2619dc6a3f542ae9c31fe0cefed846f1.svg?invert_in_darkmode&sanitize=true" align=middle width=50.62775354999999pt height=21.18721440000001pt/>, produciendo una magnetización neta nula y decaimiento exponencial en la correlación entre espines.

<p align="center"><img src="/tex/458ac51423e040010bb55568a195867c.svg?invert_in_darkmode&sanitize=true" align=middle width=164.50138815pt height=11.4155283pt/></p>

En el modelo de Gauber, los espines son seleccionados aleatoriamente cambiando su estado de <img src="/tex/76f2412b462605ef0f4aae175bb602cd.svg?invert_in_darkmode&sanitize=true" align=middle width=66.79790534999998pt height=19.1781018pt/> con una tasa que actualiza la energía. Por construcción, la magnetización no se puede conservar en cada actualización. Se pueden clasificar las actualizaciones en tres tipos de transiciones: energy-rising, energy-lowering y energy-conserving (ver fig(\ref{ads})). El energy-rising ocurre cuando un espín esta alineado con sus vecinos y el energy-lowering ocurre cuando el espín esta anti-alineado con sus vecinos. El energy-neutral, se presenta cuando la magnetización es nula localmente antes y después de la transición. El principio básico tras las transiciones de los estados está en la condición de balance detallado:

<p align="center"><img src="/tex/5699619ce6c38b239bfd577f55875c8a.svg?invert_in_darkmode&sanitize=true" align=middle width=469.9246464pt height=17.031940199999998pt/></p>  

Donde <img src="/tex/fa508b2a1400627285a9983b5f2688da.svg?invert_in_darkmode&sanitize=true" align=middle width=13.80998849999999pt height=14.15524440000002pt/> es un espín tomado aleatoriamente de la red, <img src="/tex/80f39ff0545b8ac18a89772ed6870e19.svg?invert_in_darkmode&sanitize=true" align=middle width=37.649447549999984pt height=24.65753399999998pt/> es la rata de transición y <img src="/tex/bc3986c7594a28daec566e1f3904c9d9.svg?invert_in_darkmode&sanitize=true" align=middle width=44.54118899999999pt height=24.65753399999998pt/> es la Probabilidad de Boltzmann.

<p align="center"><img src="/tex/07c6ee17da924f0d5773e1f92b0359ac.svg?invert_in_darkmode&sanitize=true" align=middle width=419.3326302pt height=36.99204465pt/></p> 

La condición de balance detallado implica que las corrientes de probabilidad que fluyen al pasar de <img src="/tex/fa508b2a1400627285a9983b5f2688da.svg?invert_in_darkmode&sanitize=true" align=middle width=13.80998849999999pt height=14.15524440000002pt/> a <img src="/tex/a3a86b506811bc5aed54061ad9e4cf77.svg?invert_in_darkmode&sanitize=true" align=middle width=26.59542269999999pt height=19.1781018pt/> y viceversa son equivalentes. Por definición, <img src="/tex/8a3f8aa018d88bc118078b83842a8d46.svg?invert_in_darkmode&sanitize=true" align=middle width=23.228404649999987pt height=22.465723500000017pt/> satisface la condición balance detallado. Consecuentemente, la evolución de los espines debe tender en tiempos grandes a un estado de equilibrio para toda temperatura positiva. Sin embargo, se deben considerar las siguientes condiciones:

<p align="center"><img src="/tex/d7c1de54328922caf6bc64a770a7f9bf.svg?invert_in_darkmode&sanitize=true" align=middle width=675.6170685pt height=165.84475544999998pt/></p>

Finalmente, se tiene que la tasa de transición en un modelo de Ising no-homogéneo (se considera que <img src="/tex/aad90aa5c5c646e48acca4d788ef29cb.svg?invert_in_darkmode&sanitize=true" align=middle width=45.21677984999998pt height=26.76175259999998pt/> y se usa la expansión en Taylor de la función exponencial), cumple:

<p align="center"><img src="/tex/0d1155199189bd94deb13141c3fba3c6.svg?invert_in_darkmode&sanitize=true" align=middle width=493.30698944999995pt height=88.1494053pt/></p>

Donde la suma es sobre los primeros vecinos al espin <img src="/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/> y la rata de la transición es la siguiente:

<p align="center"><img src="/tex/1c97a712927b7a04d87f672cdeb4d5ec.svg?invert_in_darkmode&sanitize=true" align=middle width=492.69213179999997pt height=59.1786591pt/></p>

Donde el <img src="/tex/d5d5564ce0bb9999695f32da6ba7af42.svg?invert_in_darkmode&sanitize=true" align=middle width=24.657628049999992pt height=24.65753399999998pt/> es para considerar el energy-conserving. Si se considera que <img src="/tex/fd7c45eb2515ec78286f8d1b68e23a10.svg?invert_in_darkmode&sanitize=true" align=middle width=53.89831424999999pt height=22.465723500000017pt/>, se puede ver facílmente que la rata de transición de los estados es <img src="/tex/d5d5564ce0bb9999695f32da6ba7af42.svg?invert_in_darkmode&sanitize=true" align=middle width=24.657628049999992pt height=24.65753399999998pt/> e implica que es igualmente probable tener espines con <img src="/tex/776f93672423b6ad1b8808ea2f124452.svg?invert_in_darkmode&sanitize=true" align=middle width=37.84231934999999pt height=21.18721440000001pt/> y <img src="/tex/2619dc6a3f542ae9c31fe0cefed846f1.svg?invert_in_darkmode&sanitize=true" align=middle width=50.62775354999999pt height=21.18721440000001pt/> , lo que conlleva a una magnetización nula. A temperaturas altas las fluctuaciones térmicas son privilegiadas sobre las interacciones locales aleatorizando el sistema.
