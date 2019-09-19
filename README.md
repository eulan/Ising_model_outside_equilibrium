<p align="center"><img src="/tex/53c3870a6d9ca426235d8065d8fb117e.svg?invert_in_darkmode&sanitize=true" align=middle width=236.42476605pt height=17.5342167pt/></p>

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


<p align="center"><img src="/tex/f75a928aab7b5734b580ef749a2cebc4.svg?invert_in_darkmode&sanitize=true" align=middle width=215.56056884999995pt height=11.4155283pt/></p>

En principio, se puede utilizar la ecuación maestra y calcular la distribución de probabilidad <img src="/tex/d739982f24752357c49918875935533c.svg?invert_in_darkmode&sanitize=true" align=middle width=34.74797534999998pt height=24.65753399999998pt/> en el tiempo, para luego obtener las funciones de correlación <img src="/tex/e6e2491cd1274007cdc0dbd09f68853d.svg?invert_in_darkmode&sanitize=true" align=middle width=143.64544425pt height=24.65753399999998pt/>, donde <img src="/tex/fa6b313ae87d9a77c52e6ac058051c0a.svg?invert_in_darkmode&sanitize=true" align=middle width=148.09075545pt height=24.657735299999988pt/>. Sin embargo, este proceso es muy complicado y propenso al error en t\'erminos de los metódos númericos. Por eso se va a utilizar una alternativa más simple, tratando sobre las variables de estado de espínes, se hará en primer lugar para <img src="/tex/b5d8941c501e7498e8c64c5a96142166.svg?invert_in_darkmode&sanitize=true" align=middle width=25.96371029999999pt height=24.65753399999998pt/> y luego se generalizará: 

<p align="center"><img src="/tex/b6589b61d4f8161e5f4f701515cd9688.svg?invert_in_darkmode&sanitize=true" align=middle width=561.3550008pt height=39.452455349999994pt/></p>

Por ello se tiene:

<p align="center"><img src="/tex/079edb7dba4a1473734715360904e35f.svg?invert_in_darkmode&sanitize=true" align=middle width=506.57659305pt height=16.438356pt/></p>    

Reduciendo al límite continuo, se tiene:

<p align="center"><img src="/tex/1d6e0e703d86de7515eaa6c41edd4456.svg?invert_in_darkmode&sanitize=true" align=middle width=407.15227905pt height=33.81208709999999pt/></p>

Luego aplicando promedio se tiene:

<p align="center"><img src="/tex/0da7057f66314ae70389c7474b932f52.svg?invert_in_darkmode&sanitize=true" align=middle width=414.73219424999996pt height=33.81208709999999pt/></p>

Analógamente, se tiene para <img src="/tex/961900479a097db123a34b2128eaca51.svg?invert_in_darkmode&sanitize=true" align=middle width=24.73946639999999pt height=22.465723500000017pt/>:

<p align="center"><img src="/tex/61bf085d443bd4a79c286e27ea4316c8.svg?invert_in_darkmode&sanitize=true" align=middle width=452.07000795pt height=33.81208709999999pt/></p>

También, se puede generalizar y tener la función de correlación para <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> espines:

<p align="center"><img src="/tex/fc0d82254d8f1a85e7f0d3cffc321637.svg?invert_in_darkmode&sanitize=true" align=middle width=569.3916260999999pt height=44.69878215pt/></p>

Reduciendose al límite continuo, se tiene:

<p align="center"><img src="/tex/c9dc5d5a9e9bc465506c1d1c0d0477f4.svg?invert_in_darkmode&sanitize=true" align=middle width=479.90943824999994pt height=44.69878215pt/></p>

Finalmente, se demostró las  ecuaciones que describen las dinámica del sistema en función del tiempo. Sin necesidad de recurrir directamente a la ecuación maestra.


