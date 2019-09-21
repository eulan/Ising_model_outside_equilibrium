\begin{center}
\textbf{\large Modelo de Ising-Gauber en 1D}
\end{center}

El modelo de Ising es probablemente el modelo más estudiado en mecánica estadística, en gran medida por su simplicidad y su utilidad en la comprensión de las transiciones de fase así como también por su gran rango de aplicación. En el modelo clásico de Ising, espines que existen en sitios de la red regular tienen dos posibles valores $s=\pm 1$. El Hamiltoniano del sistema es el siguiente:

\begin{equation} \label{eq1}
H=-\sum_{\langle i,j \rangle} J s_{i}s_{j}
\end{equation}

Donde la suma es sobre todos los pares de primeros vecinos. Así todo par paralelo de espines aporta al sistema  una energía $-J$ y los antiparalelos aportan $J$. Todas las propiedades de equilibrio del sistema pueden ser obtenidas a partir de la función de partición $Z=\sum e^{-\beta H}$, donde la suma es sobre todas las configuraciones de espines en el sistema, y $\beta=1/k_{B}T$ es el inverso de la temperatura. Para $J>0$, aparece el ferromágnetismo de forma espontánea por debajo de la temperatura crítica $T_{c}$ en dimensiones superiores a $d=1$ y campo externo nulo. En ese estado la magnetización es diferente de cero y espines distantes estan correlacionados. Sin embargo, por encima de la temperatura crítica $T_{c}$ los espines estan distribuidos de tal forma que existen igual cantidad de espines con $s=1$ y $s=-1$, produciendo una magnetización neta nula y decaimiento exponencial en la correlación entre espines.

\begin{center}
\textbf{Ratas de Transición}
\end{center}

En el modelo de Gauber, los espines son seleccionados aleatoriamente cambiando su estado de $s_{j} \rightarrow -s_{j}$ con una tasa que actualiza la energía. Por construcción, la magnetización no se puede conservar en cada actualización. Se pueden clasificar las actualizaciones en tres tipos de transiciones: energy-rising, energy-lowering y energy-conserving (ver fig(\ref{ads})). El energy-rising ocurre cuando un espín esta alineado con sus vecinos y el energy-lowering ocurre cuando el espín esta anti-alineado con sus vecinos. El energy-neutral, se presenta cuando la magnetización es nula localmente antes y después de la transición. El principio básico tras las transiciones de los estados está en la condición de balance detallado:

\begin{equation}
P_{eq}(s_{j}) \omega_{j}(s_{j})=P_{eq}(-s_{j}) \omega_{j}(-s_{j})
\end{equation}  

Donde $s_{j}$ es un espín tomado aleatoriamente de la red, $\omega_{j}(s)$ es la rata de transición y $P_{eq}(s)$ es la Probabilidad de Boltzmann.

\begin{equation}
P_{eq}(s_{j})=\frac{e^{-\beta H(s_{j})}}{Z}
\end{equation} 

La condición de balance detallado implica que las corrientes de probabilidad que fluyen al pasar de $s_{j}$ a $-s_{j}$ y viceversa son equivalentes. Por definición, $P_{eq}$ satisface la condición balance detallado. Consecuentemente, la evolución de los espines debe tender en tiempos grandes a un estado de equilibrio para toda temperatura positiva. Sin embargo, se deben considerar las siguientes condiciones:

\begin{itemize}
\item Como la rata de transición no está basada en algún modelo microscópico, el sistema siempre iniciará en equilibrio. Sin embargo, si el sistema se encuentra en un estado lejos del equilibrio, este tenderá a él para tiempos grandes. 
\item El sistema llegará al equilibrio en alguna temperatura positiva, ya que todos las posibles transiciones tienen asociadas una probabilidad. Sin embargo, cuando $T=0$, el energy-rising es prohibido evitando que el sistema tenga aumentos de energía. Consecuentemente, el sistema quedará atrapado en un estado de mínimo local o metaestable y nunca llegará al estado de equilibrio. 
\end{itemize}

Finalmente, se tiene que la tasa de transición en un modelo de Ising no-homogéneo (se considera que $s_{j}^{2}=1$ y se usa la expansión en Taylor de la función exponencial), cumple:

\begin{equation}
\begin{split}
\frac{\omega(s_{j})_{j}}{\omega(-s_{j})_{j}} & =\frac{P_{eq}(-s_{j})}{P_{eq}(s_{j})}=\frac{e^{-\beta(s_{j})\sum_{i} J_{ji}s_{i}}}{e^{-\beta(-s_{j})\sum_{i} J_{ji}s_{i}}}\\
 &= \frac{1-s_{j} \tanh\left(\beta \sum_{i} J_{ji} s_{i}\right)}{1+s_{j} \tanh\left(\beta \sum_{i} J_{ji} s_{i}\right)}
\end{split}
\end{equation}

Donde la suma es sobre los primeros vecinos al espin $i$ y la rata de la transición es la siguiente:

\begin{equation}
\omega_{i}(s)= \frac{1}{2} \left(1-s_{i} \tanh{ \left(\beta \sum_{j} J_{ij} s_{j}\right)} \right)
\label{lulo}
\end{equation}

Donde el $1/2$ es para considerar el energy-conserving. Si se considera que $T \rightarrow \infty$, se puede ver facílmente que la rata de transición de los estados es $1/2$ e implica que es igualmente probable tener espines con $s=1$ y $s=-1$ , lo que conlleva a una magnetización nula. A temperaturas altas las fluctuaciones térmicas son privilegiadas sobre las interacciones locales aleatorizando el sistema.

\begin{center}
\textbf{Dinamica de Glauber en una dimensión}
\end{center}

En una dimensión, considerando que $J_{ij}=J\delta_{ij}$, se tiene la siguiente tasa de transición:

\begin{equation}
\omega_{i}(s)=\frac{1}{2}\bigl(1-s_{i} \gamma \frac{s_{i+1}+s_{i-1}}{2}\bigr)
\end{equation}

Con $\gamma=\tanh(2\beta J)$. A pesar de que la tasa de Glauber es compatible con la condición de balance detallado, no es la rata de transición más general posible, pero es la única rata que soluciona el modelo de Ising. Sin embargo, cumple las siguientes propiedades de estructura:

\begin{itemize}
\item Localidad: Debido a que el Hamiltoniano considera interacción, la rata de transición debe hacerlo también $\omega(s)=\omega(s_{i},s_{i+1},s_{i-1})$.
\item Simetría traslacional: la rata es invariante bajo $i-1 \longleftrightarrow i+1$.
\item Simetría up/down: Inversión sobre los giros, es una propiedad que se observa en el hamiltoniano. Esto no es válido cuando hay campos externos.
\end{itemize}

Por lo general, se trabajará siempre con la rata de Glauber, sin ninguna restricción.

\begin{center}
\textbf{Funciones de Correlación}
\end{center}

En principio, se puede utilizar la ecuación maestra y calcular la distribución de probabilidad $P_{i}(t)$ en el tiempo, para luego obtener las funciones de correlación $S_{i,j,k,...}=\langle s_{i}s_{j}s_{k}...\rangle$, donde $\langle f(s_{i}) \rangle = \sum_{i} P(s_{i},t)$. Sin embargo, este proceso es muy complicado y propenso al error en t\'erminos de los metódos númericos. Por eso se va a utilizar una alternativa más simple, tratando sobre las variables de estado de espínes, se hará en primer lugar para $\langle s_{i} \rangle$ y luego se generalizará: 

\begin{equation}
s_{i}(t+\delta t) = \left\lbrace
\begin{array}{ll}
 s_{i}(t) & \textup{con una probabilidad: } 1-\omega_{i}(s)\delta t\\
 -s_{i}(t) & \textup{con una probabilidad: } \omega_{i}(s) \delta t
\end{array}
\right.
\end{equation}

Por ello se tiene:

\begin{equation}
s_{i}(t+\delta t) = s_{i}(t) (1-\omega_{i}(s)\delta t) - s_{i}(t) \omega_{i}(s) \delta t
\end{equation}    

Reduciendo al límite continuo, se tiene:

\begin{equation}
\frac{ds_{i}}{dt}= -2s_{i}\omega_{i}(s)
\end{equation}

Luego aplicando promedio se tiene:

\begin{equation}
\frac{dS_{i}}{dt}= -2 \langle s_{i}\omega_{i}(s) \rangle
\end{equation}

Analógamente, se tiene para $S_{i,j}$:

\begin{equation}
\frac{dS_{i,j}}{dt}= -2 \langle s_{i} s_{j}(\omega_{i}+\omega_{j})(s) \rangle
\end{equation}

También, se puede generalizar y tener la función de correlación para $n$ espines:

\begin{equation}
\prod_{n=1}^{m} s_{i_{n}}(t+\delta t) = \left\lbrace
\begin{array}{ll}
 \prod_{n=1}^{m} s_{i_{n}}(t) & \textup{con: } 1-\sum_{n=1}^{m}\omega_{i_{n}}(s)\delta t\\
 - \prod_{n=1}^{m} s_{i_{n}}(t) & \textup{con: } \sum_{n=1}^{m}\omega_{i_{n}}(s) \delta t
\end{array}
\right.
\end{equation}

Reduciendose al límite continuo, se tiene:

\begin{equation}
\frac{dS_{i_{1},i_{2},...,i_{m}}}{dt}= -2\langle \prod_{n=1}^{m} s_{i_{n}} \sum_{n=1}^{m} \omega_{i_{n}}(s) \rangle
\end{equation}

Finalmente, se demostró las  ecuaciones que describen las dinámica del sistema en función del tiempo. Sin necesidad de recurrir directamente a la ecuación maestra.


\begin{center}
\textbf{Obtención de los observables}
\end{center}

Basados en el calculos anterior se puede mostrar que en la magnetización cumple el sigueinte comportamiento:

\begin{equation}
\frac{dS_{j}}{dt}=-S_{j}+\frac{\gamma}{2}(S_{j-1}+S_{j+1})
\end{equation}

\begin{equation}
S_{k}= e^{-t}I_{k}(\gamma t)
\end{equation}

Donde $I_{k}$ es la función de Bessel de segunda especie de orden $j$ \cite{Abra}.  Para $T>0$, el espín promedio decae asintóticamente de la forma $S_{j}(t) \sim (2 \pi \gamma t)^{-1/2} e^{-(1-\gamma)t}$, con un tiempo de relajación $\tau=(1-\gamma)^{-1}$ (cuando la temperatura es nula, el tiempo de decaimiento es infinito). La magnetización $m=N\sum_{j}S_{j}$, satiface $dm/dt=-(1-\gamma)m$, donde $m$ decae exponencialmente:

\begin{equation}
m(t)=m(0)e^{-(1-\gamma)t}
\end{equation}  

Ahora, es de interes estudiar la función de correlación de pares $S_{i,j}$. La correlación entre vecinos es muy importante por su interpretación geométrica en términos de paredes de dominios. Se va considerar que dos espines antiparalelos forman una pared de dominio o cuasi-partícula. Por tanto, se puede asumir que (k,k+1) es una pared de dominio si $\frac{1}{2} (1- s_{k} s_{k+1})=1$. Así, la densidad de paredes de dominios queda dada por:

\begin{equation}
\rho = \langle \frac{1}{2} (1-s_{k}s_{k+1})\rangle = \frac{1}{2} (1-G_{1})
\end{equation} 

Por invarianza frente a traslaciones, la función de correlación, $G_{k}$, debe depender sólo de la separación entre dos espines $G_{k}=S_{i,i+k}$, por tanto la ecuación maestra toma la forma:

\begin{equation}
\frac{dG_{k}}{dt}=-2G_{k}+\gamma (G_{k-1}+G_{k+1})
\label{dG}
\end{equation}

Para $k>0$, se tiene la condición de frontera $G_{0}= \langle s_{1}^{2} \rangle=1$. Se puede mostrar que para el caso diamagnetico, y antiferromagnetico, se tiene después de algunos calculos que la densidad de primeros vecinos cumple:

\begin{equation}
\rho \sim (4 \pi t) ^{-1/2} 
\end{equation}

y con una magnetización inicial $m_{0}$:

\begin{equation}
\rho \sim (4 \pi t) ^{-1/2} (1-m_{0})^{2}
\end{equation}

En conclusión, la forma de la densidad de barreras de dominios es independiente de la magnetización inicial y en temperatura cero, la dinámica de las barreras de dominios coinciden con la de un sistema de reacción-difusión sujeto a una reacción de aniquilación: $A + A \rightarrow 0$.

\begin{center}
\textbf{Multipletes de paredes de dominio}
\end{center}

Se puede expandir el analísis de las paredes de dominio calculando la probabilidad de que se tengan dos paredes dominios consecutivos. Los pares $(k-1,k)$ y $(k,k+1)$ se encuentran si $\frac{1}{4} (1-s_{k-1}s_{k})(1-s_{k}s_{k+1})=1$. Así las densidad de dobletes es:

\begin{equation}
\begin{split}
\rho_{2} &=\left\langle \frac{1}{4} (1-s_{k-1}s_{k})(1-s_{k}s_{k+1})\right\rangle \\
&=\frac{1}{4} (1-2G_{1}+G_{2})
\end{split}
\end{equation}

Calculado $G_{1}$ y $G_{2}$, por medio de $G_{k}$ calculado anterior mente para magnetización inicial nula, la densidad de dobletes es:

\begin{equation}
\begin{split}
\rho_{2} &= \frac{1}{4} [I_{0}-I_{2}](2t) \\
&=\frac{1}{4t} e^{2t} I_{1}(2t) \sim \frac{1}{8 \sqrt{\pi t^{3}}}
\end{split}
\end{equation}

Análogamente, se tiene para la densidad de tripletes:

\begin{equation}
\rho_{3}=\left\langle \frac{1}{8} (1-s_{k-1}s_{k}) (1-s_{k}s_{k+1}) (1-s_{k+1}s_{k+2})\right\rangle
\end{equation}

Esto se puede expresar como:

\begin{equation}
\rho_{3}= \frac{1}{4}(1-4G_{1}+2G_{2}-G_{3}+\langle s_{k-1}s_{k}s_{k+1}s_{k+2}\rangle)
\end{equation}

Así para determinar de tripletes es necesario conocer la función de correlación de 4-espines. Esta relación no es trivial, la solución más natural se presenta en la condición $m_{0}=0$ y se obtiene:

\begin{equation}
\langle s_{k-1}s_{k}s_{k+1}s_{k+1} \rangle=G_{1}^{2}+G_{1}G_{3}-G_{2}^{2}
\end{equation} 

Combinando este resultados con el anterior, usando $G_{k}$ y considerando el comportamiento asintotico, se obtiene:

\begin{equation}
\rho_{3} \sim \frac{1}{8\pi t^{3} }
\end{equation}

\begin{center}
\textbf{Arqitectura}
\end{center}

Se va a contruir modelo con una red neuronal que modele las densidades de dominios y la magnetización.

Finalmente, el objetivo de todo este proyecto es recrear estos resultados numericamente con Monte Carlo Cinético (KMC) y luego contruir una red neuronal que sea capaz de basado en los calculos de KMC obtener las densidades de dominios, y la magnetización. ¡Entonces, vamos allá!



