如图1：
![图一](https://raw.githubusercontent.com/maphyca/compuational_physics_2014301020045/master/homework/diagram1.png)

以下给出f取不同值时对应的相位图
![F=1.4](https://raw.githubusercontent.com/maphyca/compuational_physics_2014301020045/master/homework/F=1.4.png)
![F=1.44]((https://raw.githubusercontent.com/maphyca/compuational_physics_2014301020045/master/homework/F=1.44.png)
![F=1.465]((https://raw.githubusercontent.com/maphyca/compuational_physics_2014301020045/master/homework/F=1.465.png)
附图1源码：
```
#define PI 3.14159265358979323846
#include <QtCharts/QChartView>
#include <QtCharts/QScatterSeries>
#include <QApplication>
#include <QMainWindow>
#include <QtCore/QtMath>
#include <QString>
#include<cmath>
 using namespace QtCharts;
int main(int argc, char *argv[])
{
     QApplication a(argc, argv);
     QScatterSeries *series0 = new QScatterSeries();
    series0->setMarkerShape(QScatterSeries::MarkerShapeCircle);
    series0->setMarkerSize(5.0);
    series0->setColor(Qt::black);
    series0->setPen(Qt::SolidLine);
    qreal  b = 0.2,vb = 0.0,t = 0.0, g = 9.8,l = 9.8, q = 0.5,F ,D=2.0/3.0,dt = 0.04;
    for(int j=0;j<=1000;j+=1){
        F=1.35+0.000135*j;
        for(int i =0;i<=5000;i++){
        vb+= (-(g/l)*qSin(b)-q*vb+F*qSin(D*t))*dt;
        b +=vb *dt;
        t+= dt;
        if(b>PI)
            b-=2*PI ;
        if(b<-PI)
            b+=2*PI ;
        if (fmod(t,(3*PI))<0.04 && t>30)
            series0->append(F,b);
    }
}
    QString A="Force";
    QString B ="Angle";
    QChart *chart = new QChart();
    chart->addSeries(series0);
    chart->createDefaultAxes();
    chart->axisX()->setTitleText(A);
    chart->axisY()->setTitleText(B);

    QChartView *chartView = new QChartView(chart);
    chartView->setRenderHint(QPainter::Antialiasing);

    QMainWindow window;
    window.resize(1080,720);
    window.setCentralWidget(chartView);
    window.show();

    return a.exec();
}
```
