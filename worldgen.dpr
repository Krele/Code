program worldgen;

{$APPTYPE CONSOLE}

uses
  SysUtils;

var A: array of array of Integer;
    N,x,y,i,p,q1,q2,e,void,r,w,t,c,L,s,wood,citycount,mountains:integer;
    earthq:real;
    f:Text;
begin
  Assign(f,'C:\map.txt');
  rewrite(f);
  Randomize;
  N:=22;                 //установим размер карты NxN
  SetLength(A,100,100);
  e:=1; //земля
  void:=0; //void
  r:=4;  //скала
  w:=3;  //вода
  t:=7;  //лес
  c:=2;  //город
  L:=6;  //локация
  s:=8;  //локация

  for x:=0 to 10+N-1 do
  for y:=0 to 10+N-1 do
  A[x,y]:=void;             //заполним карту пустотой
  earthq:=0;

  while earthq<0.57*N*(N+10) do           //вставляем куски земли
   begin
    for x:=2 to 10+N-3 do
    for y:=2 to N-3 do
     begin
     if A[x,y]=void then
       begin
       if Random(1000)<=5 then
         begin
         A[x,y]:=e;
         A[x+1,y]:=e;
         A[x,y+1]:=e;
         A[x-1,y]:=e;
         A[x,y-1]:=e;
         A[x-1,y+1]:=e;
         A[x+1,y-1]:=e;
         earthq:=earthq+7;
         end;
       if Random(1000)<=5 then
         begin
         A[x,y]:=e;
         A[x+1,y]:=e;
         A[x,y+1]:=e;
         A[x-1,y]:=e;
         earthq:=earthq+4;
         end;
       if Random(1000)<=5 then
         begin
         A[x,y]:=e;
         earthq:=earthq+1;
        end
      end;
    end;
  end;                           //конец земли

   for x:=2 to N-3+10 do   //вторая прогонка по ячейке
   for y:=2 to N-3 do
    begin

     if (A[x,y]=void) and (A[x,y-1]+A[x,y+1]+A[x-1,y]+A[x+1,y]+A[x-1,y+1]+A[x+1,y-1]>=4)
     then if random(100)<95 then A[x,y]:=e;

    end;
          //конец

  mountains:=0;                   //рандомные горы
  while mountains<=10 do
  begin
    for x:=2 to 10+N-3 do
    for y:=2 to N-3 do
     if (A[x,y]=e)
     and (A[x,y-1]=e)
     and (A[x+1,y-1]=e)
     and (A[x+1,y]=e)
     and (A[x,y+1]=e)
     and (A[x-1,y+1]=e)
     and (A[x-1,y]=e)
     and (A[x-1,y-1]=e)
     and (A[x+1,y+1]=e)
     then if Random(100)<5 then
    begin
    A[x,y]:=r;
    mountains:=mountains+1;
    end;
   end;                          //конец гор

            //расширение территории гор
   for i:=1 to 2 do begin
   for x:=2 to N-3+10 do
   for y:=2 to N-3 do
    begin
     if (A[x,y]=r) and (A[x,y-1]+A[x,y+1]+A[x-1,y]+A[x+1,y]+A[x-1,y+1]+A[x+1,y-1]<9)
     then A[x+random(3),y+random(3)-1]:=r;
     end;       //конец гор 2
     end;

  citycount:=0;                  //рандомный город
  while citycount<=3 do
  begin
    for x:=2 to 10+N-3 do
    for y:=2 to N-3 do
    if A[x,y]=e then if Random(1000)<5 then
    begin
    A[x,y]:=c;
    citycount:=citycount+1;
    end;
   end;                          //точка города

   while wood<0.025*N*(N+10) do  //вставляем лес
   begin
    for x:=2 to 10+N-3 do
    for y:=2 to N-3 do
     if (A[x,y]<>void) AND (A[x,y]<>r) and (A[x,y]<>c) then
     if random(100)<10 then begin
     A[x,y]:=t;
     wood:=wood+1;
     end;
     end;                //конец леса

   p:=0;                 //отрисовка результата
   earthq:=0;
   for x:=0 to N-1 do
    begin
     // Writeln;
     // Writeln(f);
      p:=p+1;
      for i:=1 to p do write(' ');
      for i:=1 to p do write(f,' ');
      if p>=2 then p:=0;
    for y:=0 to 10+N-1 do
     begin
     if A[x,y]<>0 then earthq:=earthq+1;
     write(A[y,x],' ');
     write(f,A[y,x],' ');
     end;
     Writeln;
     Writeln(f);
    end;

   Writeln('Earth percentage is ',(100*earthq)/(N*(N+10)):3:1,'%');
   Writeln('Cities percentage is ',(100*citycount)/(N*(N+10)):3:1,'%');
   Writeln('Mountains percentage is ',(100*mountains)/(N*(N+10)):3:1,'%');
   Writeln('Woods percentage is ',(100*wood)/(N*(N+10)):3:1,'%');
   Readln;
   Close(f);
end.
