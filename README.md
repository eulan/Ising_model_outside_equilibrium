<p align="center"><img src="/tex/ab92974684d1d0c64e57df27c67d32ad.svg?invert_in_darkmode&sanitize=true" align=middle width=301.77866895pt height=17.5342167pt/></p>

El modelo de Ising es probablemente el modelo más estudiado en mecánica estadística, en gran medida por su simplicidad y su utilidad en la comprensión de las transiciones de fase así como también por su gran rango de aplicación. En el modelo clásico de Ising, espines que existen en sitios de la red regular tienen dos posibles valores <img src="/tex/ac79f544ac468d9cd8eb78cb27613b1a.svg?invert_in_darkmode&sanitize=true" align=middle width=50.62775354999999pt height=21.18721440000001pt/>. El Hamiltoniano del sistema es el siguiente:

<p align="center"><img src="/tex/476e65449d95cf7c6cd1f053e5272326.svg?invert_in_darkmode&sanitize=true" align=middle width=118.1657202pt height=40.548151049999994pt/></p>

Donde la suma es sobre todos los pares de primeros vecinos. Así todo par paralelo de espines aporta al sistema  una energía <img src="/tex/81034b6c32f9c5d7adb1506259fa37c8.svg?invert_in_darkmode&sanitize=true" align=middle width=23.48178689999999pt height=22.465723500000017pt/> y los antiparalelos aportan <img src="/tex/8eb543f68dac24748e65e2e4c5fc968c.svg?invert_in_darkmode&sanitize=true" align=middle width=10.69635434999999pt height=22.465723500000017pt/>. Todas las propiedades de equilibrio del sistema pueden ser obtenidas a partir de la función de partición <img src="/tex/9398f7be2715f5f7d656029cd5bf0fc0.svg?invert_in_darkmode&sanitize=true" align=middle width=92.02568429999998pt height=27.91243950000002pt/>, donde la suma es sobre todas las configuraciones de espines en el sistema, y <img src="/tex/979db2d6ece9284957fc4d99ee71496e.svg?invert_in_darkmode&sanitize=true" align=middle width=80.28328604999999pt height=24.65753399999998pt/> es el inverso de la temperatura. Para <img src="/tex/0b5b3b3bb6d2c0b9dcc5b75bc8334b07.svg?invert_in_darkmode&sanitize=true" align=middle width=40.83319019999999pt height=22.465723500000017pt/>, aparece el ferromágnetismo de forma espontánea por debajo de la temperatura crítica <img src="/tex/f3087bed09ac6d957af8ecfe91212479.svg?invert_in_darkmode&sanitize=true" align=middle width=15.480837899999988pt height=22.465723500000017pt/> en dimensiones superiores a <img src="/tex/4cfe92e893a7541f68473ecb08419237.svg?invert_in_darkmode&sanitize=true" align=middle width=38.69280359999998pt height=22.831056599999986pt/> y campo externo nulo. En ese estado la magnetización es diferente de cero y espines distantes estan correlacionados. Sin embargo, por encima de la temperatura crítica <img src="/tex/f3087bed09ac6d957af8ecfe91212479.svg?invert_in_darkmode&sanitize=true" align=middle width=15.480837899999988pt height=22.465723500000017pt/> los espines estan distribuidos de tal forma que existen igual cantidad de espines con <img src="/tex/776f93672423b6ad1b8808ea2f124452.svg?invert_in_darkmode&sanitize=true" align=middle width=37.84231934999999pt height=21.18721440000001pt/> y <img src="/tex/2619dc6a3f542ae9c31fe0cefed846f1.svg?invert_in_darkmode&sanitize=true" align=middle width=50.62775354999999pt height=21.18721440000001pt/>, produciendo una magnetización neta nula y decaimiento exponencial en la correlación entre espines.

<p align="center"><img src="/tex/458ac51423e040010bb55568a195867c.svg?invert_in_darkmode&sanitize=true" align=middle width=164.50138815pt height=11.4155283pt/></p>

En el modelo de Gauber, los espines son seleccionados aleatoriamente cambiando su estado de <img src="/tex/76f2412b462605ef0f4aae175bb602cd.svg?invert_in_darkmode&sanitize=true" align=middle width=66.79790534999998pt height=19.1781018pt/> con una tasa que actualiza la energía. Por construcción, la magnetización no se puede conservar en cada actualización. Se pueden clasificar las actualizaciones en tres tipos de transiciones: energy-rising, energy-lowering y energy-conserving (ver fig(\ref{ads})). El energy-rising ocurre cuando un espín esta alineado con sus vecinos y el energy-lowering ocurre cuando el espín esta anti-alineado con sus vecinos. El energy-neutral, se presenta cuando la magnetización es nula localmente antes y después de la transición. El principio básico tras las transiciones de los estados está en la condición de balance detallado:

<p align="center"><img src="/tex/d3d776b458a58681a3f4d996a0733e4e.svg?invert_in_darkmode&sanitize=true" align=middle width=239.5753833pt height=17.031940199999998pt/></p>  

Donde <img src="/tex/fa508b2a1400627285a9983b5f2688da.svg?invert_in_darkmode&sanitize=true" align=middle width=13.80998849999999pt height=14.15524440000002pt/> es un espín tomado aleatoriamente de la red, <img src="/tex/80f39ff0545b8ac18a89772ed6870e19.svg?invert_in_darkmode&sanitize=true" align=middle width=37.649447549999984pt height=24.65753399999998pt/> es la rata de transición y <img src="/tex/bc3986c7594a28daec566e1f3904c9d9.svg?invert_in_darkmode&sanitize=true" align=middle width=44.54118899999999pt height=24.65753399999998pt/> es la Probabilidad de Boltzmann.

<p align="center"><img src="/tex/b6a68ea0080a4359816803989e5f3514.svg?invert_in_darkmode&sanitize=true" align=middle width=136.41867854999998pt height=36.99204465pt/></p> 

La condición de balance detallado implica que las corrientes de probabilidad que fluyen al pasar de <img src="/tex/fa508b2a1400627285a9983b5f2688da.svg?invert_in_darkmode&sanitize=true" align=middle width=13.80998849999999pt height=14.15524440000002pt/> a <img src="/tex/a3a86b506811bc5aed54061ad9e4cf77.svg?invert_in_darkmode&sanitize=true" align=middle width=26.59542269999999pt height=19.1781018pt/> y viceversa son equivalentes. Por definición, <img src="/tex/8a3f8aa018d88bc118078b83842a8d46.svg?invert_in_darkmode&sanitize=true" align=middle width=23.228404649999987pt height=22.465723500000017pt/> satisface la condición balance detallado. Consecuentemente, la evolución de los espines debe tender en tiempos grandes a un estado de equilibrio para toda temperatura positiva. Sin embargo, se deben considerar las siguientes condiciones:

<p align="center"><img src="/tex/d7c1de54328922caf6bc64a770a7f9bf.svg?invert_in_darkmode&sanitize=true" align=middle width=675.6170685pt height=165.84475544999998pt/></p>

Finalmente, se tiene que la tasa de transición en un modelo de Ising no-homogéneo (se considera que <img src="/tex/aad90aa5c5c646e48acca4d788ef29cb.svg?invert_in_darkmode&sanitize=true" align=middle width=45.21677984999998pt height=26.76175259999998pt/> y se usa la expansión en Taylor de la función exponencial), cumple:

<p align="center"><img src="/tex/333784cfa37e5194f5e1aa67ae110174.svg?invert_in_darkmode&sanitize=true" align=middle width=286.3399935pt height=88.1494053pt/></p>

Donde la suma es sobre los primeros vecinos al espin <img src="/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/> y la rata de la transición es la siguiente:

<p align="center"><img src="/tex/91b3310f78cf05cefde313b91d525692.svg?invert_in_darkmode&sanitize=true" align=middle width=285.1103343pt height=59.1786591pt/></p>

Donde el <img src="/tex/d5d5564ce0bb9999695f32da6ba7af42.svg?invert_in_darkmode&sanitize=true" align=middle width=24.657628049999992pt height=24.65753399999998pt/> es para considerar el energy-conserving. Si se considera que <img src="/tex/fd7c45eb2515ec78286f8d1b68e23a10.svg?invert_in_darkmode&sanitize=true" align=middle width=53.89831424999999pt height=22.465723500000017pt/>, se puede ver facílmente que la rata de transición de los estados es <img src="/tex/d5d5564ce0bb9999695f32da6ba7af42.svg?invert_in_darkmode&sanitize=true" align=middle width=24.657628049999992pt height=24.65753399999998pt/> e implica que es igualmente probable tener espines con <img src="/tex/776f93672423b6ad1b8808ea2f124452.svg?invert_in_darkmode&sanitize=true" align=middle width=37.84231934999999pt height=21.18721440000001pt/> y <img src="/tex/2619dc6a3f542ae9c31fe0cefed846f1.svg?invert_in_darkmode&sanitize=true" align=middle width=50.62775354999999pt height=21.18721440000001pt/> , lo que conlleva a una magnetización nula. A temperaturas altas las fluctuaciones térmicas son privilegiadas sobre las interacciones locales aleatorizando el sistema.

<p align="center"><img src="/tex/992a25aba67415cfef2af3d27af6ad96.svg?invert_in_darkmode&sanitize=true" align=middle width=328.68778304999995pt height=11.4155283pt/></p>

En una dimensión, considerando que <img src="/tex/2191e475925d75b13568d4ea96ae24a1.svg?invert_in_darkmode&sanitize=true" align=middle width=71.36790869999999pt height=22.831056599999986pt/>, se tiene la siguiente tasa de transición:

<p align="center"><img src="/tex/96cf7f2802215139454153c55efadd3e.svg?invert_in_darkmode&sanitize=true" align=middle width=220.1223684pt height=32.990165999999995pt/></p>

Con <img src="/tex/d08f81a1fd370490ee1b0ad2f1936a07.svg?invert_in_darkmode&sanitize=true" align=middle width=106.08483104999999pt height=24.65753399999998pt/>. A pesar de que la tasa de Glauber es compatible con la condición de balance detallado, no es la rata de transición más general posible, pero es la única rata que soluciona el modelo de Ising. Sin embargo, cumple las siguientes propiedades de estructura:

<p align="center"><img src="/tex/3e82001febb9bb08e28745f765c79c82.svg?invert_in_darkmode&sanitize=true" align=middle width=675.61704705pt height=119.81735864999999pt/></p>

Por lo general, se trabajará siempre con la rata de Glauber, sin ninguna restricción.

<p align="center"><img src="/tex/ed51ffdb1fb53035dd8f724397e4acb4.svg?invert_in_darkmode&sanitize=true" align=middle width=208.2090087pt height=11.4155283pt/></p>

En principio, se puede utilizar la ecuación maestra y calcular la distribución de probabilidad <img src="/tex/d739982f24752357c49918875935533c.svg?invert_in_darkmode&sanitize=true" align=middle width=34.74797534999998pt height=24.65753399999998pt/> en el tiempo, para luego obtener las funciones de correlación <img src="/tex/e6e2491cd1274007cdc0dbd09f68853d.svg?invert_in_darkmode&sanitize=true" align=middle width=143.64544425pt height=24.65753399999998pt/>, donde <img src="/tex/fa6b313ae87d9a77c52e6ac058051c0a.svg?invert_in_darkmode&sanitize=true" align=middle width=148.09075545pt height=24.657735299999988pt/>. Sin embargo, este proceso es muy complicado y propenso al error en t\'erminos de los metódos númericos. Por eso se va a utilizar una alternativa más simple, tratando sobre las variables de estado de espínes, se hará en primer lugar para <img src="/tex/b5d8941c501e7498e8c64c5a96142166.svg?invert_in_darkmode&sanitize=true" align=middle width=25.96371029999999pt height=24.65753399999998pt/> y luego se generalizará: 

<p align="center"><img src="/tex/e8f10b35303928ff7c26148b8482fe89.svg?invert_in_darkmode&sanitize=true" align=middle width=412.24435725pt height=39.452455349999994pt/></p>

Por ello se tiene:

<p align="center"><img src="/tex/5678fba231827906b5134fc7fa850bef.svg?invert_in_darkmode&sanitize=true" align=middle width=312.87945644999996pt height=16.438356pt/></p>    

Reduciendo al límite continuo, se tiene:

<p align="center"><img src="/tex/c2c3b281900b1f7030aac4af55f71646.svg?invert_in_darkmode&sanitize=true" align=middle width=116.00320545pt height=33.81208709999999pt/></p>

Luego aplicando promedio se tiene:

<p align="center"><img src="/tex/f3f3c3e2fd93bbdf05d38869d4494658.svg?invert_in_darkmode&sanitize=true" align=middle width=131.16306555pt height=33.81208709999999pt/></p>

Analógamente, se tiene para <img src="/tex/961900479a097db123a34b2128eaca51.svg?invert_in_darkmode&sanitize=true" align=middle width=24.73946639999999pt height=22.465723500000017pt/>:

<p align="center"><img src="/tex/ec847c4be3b6e5b673bc0a0ed3fb18cc.svg?invert_in_darkmode&sanitize=true" align=middle width=205.83870285pt height=33.81208709999999pt/></p>

También, se puede generalizar y tener la función de correlación para <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> espines:

<p align="center"><img src="/tex/e1db817c8550ee9e6c907f6bddcd31bc.svg?invert_in_darkmode&sanitize=true" align=middle width=428.3176309499999pt height=44.69878215pt/></p>

Reduciendose al límite continuo, se tiene:

<p align="center"><img src="/tex/4eff8a9c01dcc89533a7e8792244f483.svg?invert_in_darkmode&sanitize=true" align=middle width=261.5175552pt height=44.69878215pt/></p>

Finalmente, se demostró las  ecuaciones que describen las dinámica del sistema en función del tiempo. Sin necesidad de recurrir directamente a la ecuación maestra.


<p align="center"><img src="/tex/4896512fa07461af9674486714c33e72.svg?invert_in_darkmode&sanitize=true" align=middle width=238.90974525000001pt height=11.4155283pt/></p>

Basados en el calculos anterior se puede mostrar que en la magnetización cumple el sigueinte comportamiento:

<p align="center"><img src="/tex/6d16abfdf7bde41de29970be2853c33c.svg?invert_in_darkmode&sanitize=true" align=middle width=213.06421949999998pt height=33.81208709999999pt/></p>

<p align="center"><img src="/tex/d7e58b7d9f41f37f996134fd0d0a3e9d.svg?invert_in_darkmode&sanitize=true" align=middle width=107.26071015pt height=18.0201615pt/></p>

Donde <img src="/tex/f91c599de18e4b480b576b52c79763a4.svg?invert_in_darkmode&sanitize=true" align=middle width=14.49208034999999pt height=22.465723500000017pt/> es la función de Bessel de segunda especie de orden <img src="/tex/36b5afebdba34564d884d347484ac0c7.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/> \cite{Abra}.  Para <img src="/tex/24b11c4825206fcdba6367bc6555f22f.svg?invert_in_darkmode&sanitize=true" align=middle width=42.02615174999998pt height=22.465723500000017pt/>, el espín promedio decae asintóticamente de la forma <img src="/tex/def79e49853c252f906f08a4e768123f.svg?invert_in_darkmode&sanitize=true" align=middle width=192.51364769999998pt height=29.190975000000005pt/>, con un tiempo de relajación <img src="/tex/da1717404fb05118057b6a8afc159299.svg?invert_in_darkmode&sanitize=true" align=middle width=98.31072734999998pt height=26.76175259999998pt/> (cuando la temperatura es nula, el tiempo de decaimiento es infinito). La magnetización <img src="/tex/0b1cd96a89f2a1f2348940c266be2c8c.svg?invert_in_darkmode&sanitize=true" align=middle width=97.29250574999999pt height=24.657735299999988pt/>, satiface <img src="/tex/ebb0ddbff769a41862f83cde8993d0ac.svg?invert_in_darkmode&sanitize=true" align=middle width=145.35619394999998pt height=24.65753399999998pt/>, donde <img src="/tex/0e51a2dede42189d77627c4d742822c3.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/> decae exponencialmente:

<p align="center"><img src="/tex/de2caccb6fd7f3aafdcbd30b8f902b27.svg?invert_in_darkmode&sanitize=true" align=middle width=148.1173023pt height=19.526994300000002pt/></p>  

Ahora, es de interes estudiar la función de correlación de pares <img src="/tex/961900479a097db123a34b2128eaca51.svg?invert_in_darkmode&sanitize=true" align=middle width=24.73946639999999pt height=22.465723500000017pt/>. La correlación entre vecinos es muy importante por su interpretación geométrica en términos de paredes de dominios. Se va considerar que dos espines antiparalelos forman una pared de dominio o cuasi-partícula. Por tanto, se puede asumir que (k,k+1) es una pared de dominio si <img src="/tex/b463c25effe0e2ea10e2f71c3923524b.svg?invert_in_darkmode&sanitize=true" align=middle width=127.98857114999997pt height=27.77565449999998pt/>. Así, la densidad de paredes de dominios queda dada por:

<p align="center"><img src="/tex/7fc1de3d92ca5ab629e1471fa9defd02.svg?invert_in_darkmode&sanitize=true" align=middle width=240.16990635000002pt height=32.990165999999995pt/></p> 

Por invarianza frente a traslaciones, la función de correlación, <img src="/tex/243ff7a534430724ea3bec1ed658c741.svg?invert_in_darkmode&sanitize=true" align=middle width=20.190673799999992pt height=22.465723500000017pt/>, debe depender sólo de la separación entre dos espines <img src="/tex/3a0b9da2198e1db245eb8835e401c7aa.svg?invert_in_darkmode&sanitize=true" align=middle width=83.57347844999998pt height=22.465723500000017pt/>, por tanto la ecuación maestra toma la forma:

<p align="center"><img src="/tex/f378427c01f2813b2eac6cb5551de67c.svg?invert_in_darkmode&sanitize=true" align=middle width=233.3632851pt height=33.81208709999999pt/></p>

Para <img src="/tex/f9bbd08bf846520586581437c960abac.svg?invert_in_darkmode&sanitize=true" align=middle width=39.21220214999999pt height=22.831056599999986pt/>, se tiene la condición de frontera <img src="/tex/959646b8f0d48a8dcea9a697cef75241.svg?invert_in_darkmode&sanitize=true" align=middle width=100.21894739999999pt height=26.76175259999998pt/>. Se puede mostrar que para el caso diamagnetico, y antiferromagnetico, se tiene después de algunos calculos que la densidad de primeros vecinos cumple:

<p align="center"><img src="/tex/51ebde1a8c51cae50e2e22922eb04c7e.svg?invert_in_darkmode&sanitize=true" align=middle width=97.43165189999999pt height=19.526994300000002pt/></p>

y con una magnetización inicial <img src="/tex/fd9461a2135ca0ed5af7d494c65252b7.svg?invert_in_darkmode&sanitize=true" align=middle width=20.985647099999987pt height=14.15524440000002pt/>:

<p align="center"><img src="/tex/b6156ee727c610d191b8081ecb79d899.svg?invert_in_darkmode&sanitize=true" align=middle width=167.70945509999999pt height=19.526994300000002pt/></p>

En conclusión, la forma de la densidad de barreras de dominios es independiente de la magnetización inicial y en temperatura cero, la dinámica de las barreras de dominios coinciden con la de un sistema de reacción-difusión sujeto a una reacción de aniquilación: <img src="/tex/3b4410c0e0d21ba84b229ecc2302c33a.svg?invert_in_darkmode&sanitize=true" align=middle width=78.53859749999998pt height=22.465723500000017pt/>.

<p align="center"><img src="/tex/24f834305c63fa68c286e4c7fc54f5fe.svg?invert_in_darkmode&sanitize=true" align=middle width=286.65839895pt height=14.611878599999999pt/></p>

Se puede expandir el analísis de las paredes de dominio calculando la probabilidad de que se tengan dos paredes dominios consecutivos. Los pares <img src="/tex/24e6eeae74f33fe17ac316d45b6de731.svg?invert_in_darkmode&sanitize=true" align=middle width=66.55244144999999pt height=24.65753399999998pt/> y <img src="/tex/6e32e88434a5681bd004ab500233b744.svg?invert_in_darkmode&sanitize=true" align=middle width=66.55244144999999pt height=24.65753399999998pt/> se encuentran si <img src="/tex/1682f23c4004024f702f8cd46f4199d1.svg?invert_in_darkmode&sanitize=true" align=middle width=217.4977926pt height=27.77565449999998pt/>. Así las densidad de dobletes es:

<p align="center"><img src="/tex/840ae159a99f976daecbb6de6059bfe4.svg?invert_in_darkmode&sanitize=true" align=middle width=253.44877139999997pt height=79.0179555pt/></p>

Calculado <img src="/tex/b598a01b0b2876cf6751005227ef9149.svg?invert_in_darkmode&sanitize=true" align=middle width=19.477190699999987pt height=22.465723500000017pt/> y <img src="/tex/82588ea8e81c6c10208fabda9d31b846.svg?invert_in_darkmode&sanitize=true" align=middle width=19.477190699999987pt height=22.465723500000017pt/>, por medio de <img src="/tex/243ff7a534430724ea3bec1ed658c741.svg?invert_in_darkmode&sanitize=true" align=middle width=20.190673799999992pt height=22.465723500000017pt/> calculado anterior mente para magnetización inicial nula, la densidad de dobletes es:

<p align="center"><img src="/tex/b0788754e106e9b0900015d35627c4af.svg?invert_in_darkmode&sanitize=true" align=middle width=186.50579639999998pt height=76.56729134999999pt/></p>

Análogamente, se tiene para la densidad de tripletes:

<p align="center"><img src="/tex/34da5ea9d774e0b6108b21f7dd909570.svg?invert_in_darkmode&sanitize=true" align=middle width=359.41928055pt height=39.452455349999994pt/></p>

Esto se puede expresar como:

<p align="center"><img src="/tex/7468f43f9820983585b759890c7836fb.svg?invert_in_darkmode&sanitize=true" align=middle width=354.73399995pt height=32.990165999999995pt/></p>

Así para determinar de tripletes es necesario conocer la función de correlación de 4-espines. Esta relación no es trivial, la solución más natural se presenta en la condición <img src="/tex/6ffc6984e992370cb17dd3ef6670ff7c.svg?invert_in_darkmode&sanitize=true" align=middle width=51.94440074999999pt height=21.18721440000001pt/> y se obtiene:

<p align="center"><img src="/tex/a5bad24579961160a31a5286f4a3bff8.svg?invert_in_darkmode&sanitize=true" align=middle width=268.5480039pt height=18.312383099999998pt/></p> 

Combinando este resultados con el anterior, usando <img src="/tex/243ff7a534430724ea3bec1ed658c741.svg?invert_in_darkmode&sanitize=true" align=middle width=20.190673799999992pt height=22.465723500000017pt/> y considerando el comportamiento asintotico, se obtiene:

<p align="center"><img src="/tex/764945a75a6b46e19abbff1d48db2f22.svg?invert_in_darkmode&sanitize=true" align=middle width=71.25339869999999pt height=32.990165999999995pt/></p>

<p align="center"><img src="/tex/108190c629d67b5874643ab2b63b3175.svg?invert_in_darkmode&sanitize=true" align=middle width=96.5520468pt height=14.611878599999999pt/></p>

Se va a contruir modelo con una red neuronal que modele las densidades de correlaciones y la magnetización.

<p align="center"><img src="https://github.com/eulan/Ising_model_outside_equilibrium/blob/master/neural-network_page-0001.jpg" align=middle width=500pt height=300pt/></p>

Finalmente, el objetivo de todo este proyecto es recrear estos resultados numericamente con Monte Carlo Cinético (KMC) y luego contruir una red neuronal que sea capaz de basado en los calculos de KMC obtener las densidades de dominios, y la magnetización. ¡Entonces, vamos allá!

<p align="center"><img src="/tex/b61b01e03ef0d0cfc41cc55e716b193b.svg?invert_in_darkmode&sanitize=true" align=middle width=90.00408285pt height=11.4155283pt/></p>

<p align="center"><img src="https://github.com/eulan/Ising_model_outside_equilibrium/blob/master/result%20(1).jpg" align=middle width=700pt height=500pt/></p>

Se modelo, desde el punto de vista teórico y computacional desde Deep Learning, utilizando una red neuronal de N inputs, 2*N hidden layers, 2*N hidden layer y 4 outputs. Donde el input sería la posición de los espines en cada sitio, en un arreglo unidimensional, y los output serían la magnetización, y las correlaciones recientemente calculadas. Como se podía ver en la gráfica anterior.



