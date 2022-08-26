#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
import epy_module_0  # embedded python module
import osmosdr
import time
import threading
from gnuradio import qtgui

class SweeperGNURadio(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "SweeperGNURadio")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.funcTime = funcTime = 0
        self.func = func = 0
        self.tiempo = tiempo = epy_module_0.funTime(funcTime)
        self.freq = freq = epy_module_0.sweeper(func)
        self.vel = vel = epy_module_0.vel(func)
        self.timee = timee = tiempo
        self.samp_rate = samp_rate = 32000
        self.freqq = freqq = freq

        ##################################################
        # Blocks
        ##################################################
        self.bloqueTime = blocks.probe_signal_c()
        self.bloqueSignal = blocks.probe_signal_c()
        self._timee_tool_bar = Qt.QToolBar(self)

        if None:
            self._timee_formatter = None
        else:
            self._timee_formatter = lambda x: str(x)

        self._timee_tool_bar.addWidget(Qt.QLabel('Tiempo' + ": "))
        self._timee_label = Qt.QLabel(str(self._timee_formatter(self.timee)))
        self._timee_tool_bar.addWidget(self._timee_label)
        self.top_grid_layout.addWidget(self._timee_tool_bar)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(False)

        self.qtgui_waterfall_sink_x_0.disable_legend()


        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        self.qtgui_time_sink_x_0.disable_legend()

        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['dark green', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + "hackrf=0,bias=1"
        )
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
        def _funcTime_probe():
            while True:

                val = self.bloqueTime.level()
                try:
                    self.set_funcTime(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (1))
        _funcTime_thread = threading.Thread(target=_funcTime_probe)
        _funcTime_thread.daemon = True
        _funcTime_thread.start()

        def _func_probe():
            while True:

                val = self.bloqueSignal.level()
                try:
                    self.set_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (vel))
        _func_thread = threading.Thread(target=_func_probe)
        _func_thread.daemon = True
        _func_thread.start()

        self._freqq_tool_bar = Qt.QToolBar(self)

        if None:
            self._freqq_formatter = None
        else:
            self._freqq_formatter = lambda x: eng_notation.num_to_str(x)

        self._freqq_tool_bar.addWidget(Qt.QLabel('Frecuencia' + ": "))
        self._freqq_label = Qt.QLabel(str(self._freqq_formatter(self.freqq)))
        self._freqq_tool_bar.addWidget(self._freqq_label)
        self.top_grid_layout.addWidget(self._freqq_tool_bar)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.bloqueSignal, 0))
        self.connect((self.osmosdr_source_0, 0), (self.bloqueTime, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "SweeperGNURadio")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_funcTime(self):
        return self.funcTime

    def set_funcTime(self, funcTime):
        self.funcTime = funcTime
        self.set_tiempo(epy_module_0.funTime(self.funcTime))

    def get_func(self):
        return self.func

    def set_func(self, func):
        self.func = func
        self.set_freq(epy_module_0.sweeper(self.func))
        self.set_vel(epy_module_0.vel(self.func))

    def get_tiempo(self):
        return self.tiempo

    def set_tiempo(self, tiempo):
        self.tiempo = tiempo
        self.set_timee(self._timee_formatter(self.tiempo))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_freqq(self._freqq_formatter(self.freq))
        self.osmosdr_source_0.set_center_freq(self.freq, 0)

    def get_vel(self):
        return self.vel

    def set_vel(self, vel):
        self.vel = vel

    def get_timee(self):
        return self.timee

    def set_timee(self, timee):
        self.timee = timee
        Qt.QMetaObject.invokeMethod(self._timee_label, "setText", Qt.Q_ARG("QString", self.timee))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_freqq(self):
        return self.freqq

    def set_freqq(self, freqq):
        self.freqq = freqq
        Qt.QMetaObject.invokeMethod(self._freqq_label, "setText", Qt.Q_ARG("QString", self.freqq))



def main(top_block_cls=SweeperGNURadio, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
