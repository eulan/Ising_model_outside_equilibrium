module KMClib
IMPLICIT NONE
integer, parameter ::   N=100,Tiempo=800
integer, parameter :: NR=100
DOUBLE PRECISION, PARAMETER :: Pi = 4.0d0*ATAN(1.0d0)
double precision, parameter :: beta=0.1, Jt=1,g=1!tanh(2*beta*Jt)


!Counters

double precision t,dt,wup,wdown
INTEGER :: I, J, K, II, JJ, KK, IP,ij

end module KMClib


program Ising
use KMClib
implicit none
real :: ran2,per
integer :: idum,a,b,c,aux

double precision, dimension(N) :: Lte
double precision, dimension(tiempo) :: rou,m,time,rou2,rou3,phi
double precision, dimension(tiempo) :: timeR,mR,rouR,rouR2,rouR3,phiR
double precision :: Gmed,Gmed2,Gmed3,mmed
double precision :: ajax,xprom,raja
integer, dimension(N) :: xciu,xcfu,Ns,NsR
integer :: ncup,s 

open (199, file='lte_test.csv')
open (200, file='mag.dat')
open (198, file='rou.dat')
open (197, file='rou2.dat')
open (196, file='rou3.dat')
open (195, file='Ns.dat')

timeR=0

do ij=1,nr

idum = -ij

Lte=0
mmed=0
	xciu=0
	xcfu=0

	t=0
	dt=0
	m=0
	time=0
	Gmed=0

	do j=1,N
		if(ran2(idum).gt.0.5)then
		Lte(j)=-1
		else
		Lte(j)=1
		end if
	write(199,"(F8.3,',')", advance = "No") Lte(j)
	end do
	write(199,*) t
	
	write(*,*) ij,"bambam",g

	do jj=1,Tiempo
		kk=int(per(int((N+1)*ran2(idum)),N))
		a=int(per(kk,N))
		b=int(per(kk+1,N))
		c=int(per(kk-1,N))
		wup=0.5d0*(1-g*Lte(a)*0.5d0*(Lte(c)+Lte(b)))
		wdown=0.5d0*(1+g*Lte(a)*0.5d0*(Lte(c)+Lte(b)))	

	if(ran2(idum).lt.wup)then
	Lte(a)=-Lte(a)
	else if(ran2(idum).ge.wup)then
	Lte(a)=Lte(a)
	end if

	if(ran2(idum).ne.0)then
		dt=Log(1/ran2(idum))
	else
		dt=0.0d0
	end if	
	t=t+dt/N
	time(jj)=t

		do j=1,N
		write(199,"(F8.3,',')", advance = "No") Lte(j)
		end do
		write(199,*) t

    do i=1,N
		Gmed= Gmed+1.0d0*Lte(i)*Lte(int(per(i+1,N)))
		Gmed2= Gmed2+1.0d0*Lte(i)*Lte(int(per(i+2,N)))
		Gmed3= Gmed3+1.0d0*Lte(i)*Lte(int(per(i+3,N)))
		
		end do

		Gmed=Gmed/N
      	Gmed2=Gmed2/N
		Gmed3=Gmed3/N

		rou3(jj)=0.25*(1-3*Gmed+2*Gmed2-Gmed3)
 		rou3(jj)=rou3(jj) + 0.25*(Gmed**2+Gmed*Gmed3-Gmed2**2)
		rou2(jj)=0.25*(1-2*Gmed+Gmed2)
		rou(jj)=0.5*(1-Gmed)
	
		do ii=1,N
		m(jj)=m(jj)+Lte(ii)
		end do
        
    end do
        
        ncup=0
	do i=1,N

		if(i.eq.1.and.Lte(i)*Lte(N).gt.0)then
			ncup=1
			xciu(i)=1
			goto 125
		end if
		
		if(Lte(i)*Lte(i-1).lt.0.and.Lte(i)*Lte(i+1).gt.0)then
			ncup=ncup+1
			xciu(ncup)=i
		end if
		
		if(Lte(i)*Lte(i-1).gt.0.and.Lte(i)*Lte(i+1).lt.0)then
			xcfu(ncup)=i
		end if
		
		if(i.eq.N.and.Lte(i)*Lte(i-1).lt.0)then
			xcfu(ncup)=N+1
			goto 125
		end if	
        
125 continue
	end do

if(Lte(i)*Lte(N).gt.0)then
	xciu(1)=xciu(N)
	ncup=ncup-1
	end if

	do i=1, ncup
		if(xcfu(i)-xciu(i).gt.0)then
		s=xcfu(i)-xciu(i)
		else
		s=N+xcfu(i)-xciu(i)
		end if
		Ns(s)=Ns(s)+1
	end do


end do

do jj=1,Tiempo
		rou(jj)=rou(jj)/NR
		rou2(jj)=rou2(jj)/NR
		rou3(jj)=rou3(jj)/NR
		m(jj)=m(jj)/(NR*N)
		time(jj)=time(jj)/(NR*N)

	write(200,*) time(jj),m(jj)
	write(198,*) time(jj),rou(jj)
	write(197,*) time(jj),rou2(jj)
	write(196,*) time(jj),rou3(jj)

	end do

	raja=0.0d0
	ajax=0.0d0
	xprom=0.0d0

	do i=1,int(0.5*N)
	if(NsR(i).ne.0)then
	ajax=ajax+1.0d0*i*NsR(i)
	raja=raja+1.0d0*NsR(i)
	end if
	end do

	xprom=ajax/raja

	do i=1,int(0.5*N)
	if(NsR(i).ne.0)then 
	write(195,*) (1.0d0*i)/xprom, (xprom*1.0d0*NsR(i))/raja
	end if
	end do


! mpif90 ising.f95 -o aver
!mpirun -np 2 ./aver

end program

FUNCTION RAN2(IDUM)
        INTEGER idum,IM1,IM2,IMM1,IA1,IQ1,IQ2,IR1,IR2,NTAB,NDIV
	REAL RAN2,AM,EPS,RNMX
	PARAMETER (IM1=2147483563,IM2=2147483399,AM=1./     IM1,IMM1=IM1-1)
	PARAMETER    (IA1=40014,IA2=40692,IQ1=53688,IQ2=52744,IR1=12211)
	PARAMETER (IR2=3791,NTAB=32,NDIV=1+IMM1/NTAB,EPS=1.2e-7)
	PARAMETER(RNMX=1.-EPS)
	INTEGER idum2,j,k,iv(NTAB),iy
	SAVE iv,iy,idum2
	DATA idum2/123456789/,iv/NTAB*0/,iy/0/
	if(idum.le.0)then
	idum=max(-idum,1)
	idum2=idum
	do j=NTAB+8,1,-1
		k=idum/IQ1
		idum=IA1*(idum-k*IQ1)-k*IR1
		if (idum.lt.0) idum=idum+IM1
		if (j.le.NTAB) iv(j)=idum
	end do
	iy=iv(1)
	end if
	k=idum/IQ1
	idum=IA1*(idum-k*IQ1)-k*IR1
	if (idum.lt.0) idum=idum+IM1
	k=idum2/IQ2
	idum2=IA2*(idum2-k*IQ2)-k*IR2
	if (idum2.lt.0) idum2=idum2+IM2
	j=1+iy/NDIV
	iy=iv(j)-idum2
	iv(j)=idum
	if(iy.lt.1)iy=iy+IMM1
	ran2=min(AM*iy,RNMX)
	return
	end


	FUNCTION PER(posx,Lim)
	INTEGER posx,lim
	if(posx.gt.Lim)then
	PER=posx-Lim
        end if
	if(posx.le.0)then
	PER=posx+Lim
         end if
	if(posx.gt.0.and.posx.le.LIM)then
	PER=posx
        end if
	return 
	end

