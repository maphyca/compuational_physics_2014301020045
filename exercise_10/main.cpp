#define PI 3.14159265358979323846
#include "mainwindow.h"
#include <QApplication>
#include <QtCharts/QChartView>
#include <QtCharts/QLineSeries>
#include <QtCharts/QScatterSeries>
#include <QtCore/QtMath>
#include <QString>
QT_CHARTS_USE_NAMESPACE
int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    MainWindow w;
    QLineSeries *series0 = new QLineSeries();
    QLineSeries *series2 = new QLineSeries();
    QLineSeries *series4 = new QLineSeries();
    QScatterSeries *series1 = new QScatterSeries();
    QScatterSeries *series3 = new QScatterSeries();
    QScatterSeries *series5 = new QScatterSeries();
    qreal r1,r2,r3,a1,a2,a3,x1,x2,x3,y1,y2,y3,vx1,vx2,vx3,vy1,vy2,vy3,dt=0.0001,a=0.0008,t=0,e3=0.85,e1=0.15,e2=0.45,theta1,theta2,theta3;
    x1=x2=x3=-0.39*(1-0.15);
    a1=-x1/(1-e1);
    a2=-x2/(1-e2);
    a3=-x3/(1-e3);
    y1=y2=y3=0;
    vx1=vx2=vx3=0;
    vy1=qSqrt((4*PI*PI*(1+e1))/(a1*(1-e1)));
    vy2=qSqrt((4*PI*PI*(1+e2))/(a2*(1-e2)));
    vy3=qSqrt((4*PI*PI*(1+e3))/(a3*(1-e3)));
    for(int i=0;i<100000;i++){
        r1=qPow(x1*x1+y1*y1,0.5);
        r2=qPow(x2*x2+y2*y2,0.5);
        r3=qPow(x3*x3+y3*y3,0.5);
        vx1+=-4*PI*PI*x1*dt/(qPow(r1,3))*(1+a/(r1*r1));
        vy1+=-4*PI*PI*y1*dt/(qPow(r1,3))*(1+a/(r1*r1));
        x1+=vx1*dt;
        y1+=vy1*dt;
        vx2+=-4*PI*PI*x2*dt/(qPow(r2,3))*(1+a/(r2*r2));
        vy2+=-4*PI*PI*y2*dt/(qPow(r2,3))*(1+a/(r2*r2));
        x2+=vx2*dt;
        y2+=vy2*dt;
        vx3+=-4*PI*PI*x3*dt/(qPow(r3,3))*(1+a/(r3*r3));
        vy3+=-4*PI*PI*y3*dt/(qPow(r3,3))*(1+a/(r3*r3));
        x3+=vx3*dt;
        y3+=vy3*dt;
        t+=dt;
        if(qAbs(x1*vx1+y1*vy1)<0.001 && r1>0.39){
        theta1=qAcos(x1/r1)*180/PI;
        series0->append(t,theta1);
        series1->append(t,theta1);
        }
        if(qAbs(x2*vx2+y2*vy2)<0.001 && r2>0.39){
        theta2=qAcos(x2/r2)*180/PI;
        series2->append(t,theta2);
        series3->append(t,theta2);
        }
        if(qAbs(x3*vx3+y3*vy3)<0.001 && r3>0.39){
        theta3=qAcos(x3/r3)*180/PI;
        series4->append(t,theta3);
        series5->append(t,theta3);
        }
    }

    QChart *chart = new QChart();
    chart->addSeries(series0);
    chart->addSeries(series1);
   chart->addSeries(series2);
    chart->addSeries(series3);
    chart->addSeries(series4);
    chart->addSeries(series5);
    chart->setTitle("Simulation of the precession of Mercury");
    chart->createDefaultAxes();
    chart->setDropShadowEnabled(false);
    chart->legend()->setVisible(false);
//   chart->setAnimationOptions(QChart::SeriesAnimations);
//   chart->setAnimationDuration(5000);
    chart->axisX()->setRange(0,10);
    chart->axisY()->setRange(0,90);
    QChartView *chartView = new QChartView(chart);
    w.setCentralWidget(chartView);
    w.resize(720, 720);
    w.show();
    w.show();

    return app.exec();
}
