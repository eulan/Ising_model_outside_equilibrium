#Modelo de Ising-Gauber

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
