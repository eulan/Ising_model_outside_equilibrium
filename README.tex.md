\begin{center}
\textbf{\large Modelo de Ising-Gauber}
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
\textbf{Functiones de Correlación}
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


