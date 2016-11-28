#define PI 3.14159265358979323846
#include "mainwindow.h"
#include <QApplication>
#include <QtCharts/QChartView>
#include <QtCharts/QScatterSeries>
#include <QtCore/QtMath>
#include <QString>
QT_CHARTS_USE_NAMESPACE
int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    MainWindow w;
    QScatterSeries *series0 = new QScatterSeries();
    series0->setName("a=0.0008");
    series0->setMarkerShape(QScatterSeries::MarkerShapeCircle);
    series0->setPen(Qt::SolidLine);
    series0->setColor(Qt::black);
    series0->setMarkerSize(1);
    qreal x=0.47,y=0,vx=0,vy=8.2,dt=0.0001,a=0.0008,theta=0,t=0;
    for(int i=0;i<10000;i++){
        vx+=-4*PI*PI*x*dt/(qPow(x*x+y*y,1.5))*(1+a/(x*x+y*y));
        vy+=-4*PI*PI*y*dt/(qPow(x*x+y*y,1.5))*(1+a/(x*x+y*y));
        x+=vx*dt;
        y+=vy*dt;
        t+=dt;
        theta=qAcos(x/(x*x+y*y))*180/PI;
        series0->append(x,y);
    }
    QChart *chart = new QChart();
    chart->addSeries(series0);
    chart->setTitle("Simulation of the precession of Mercury");
    chart->createDefaultAxes();
    chart->setDropShadowEnabled(false);
//    chart->setAnimationOptions(QChart::SeriesAnimations);
//    chart->setAnimationDuration(20000);
    chart->axisX()->setRange(-0.5,0.5);
   chart->axisY()->setRange(-0.5,0.5);
    QChartView *chartView = new QChartView(chart);
    w.setCentralWidget(chartView);
    w.resize(720, 720);
    w.show();
    w.show();

    return app.exec();
}
