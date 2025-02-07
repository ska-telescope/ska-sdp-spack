### Author: dag@wieers.com
import os

class dool_plugin(dool):
    """
    CPU frequency in percentage as reported by ACPI.
    """

    def __init__(self):
        self.name = 'frequency'
        self.type = 'p'
        self.width = 4
        self.scale = 34

    def check(self):
        for cpu in glob.glob('/sys/devices/system/cpu/cpu[0-9]*'):
            if not os.access(cpu+'/cpufreq/scaling_cur_freq', os.R_OK):
                raise Exception('Cannot access acpi %s frequency information' % os.path.basename(cpu))

    def vars(self):
        ret = []
        for name in glob.glob('/sys/devices/system/cpu/cpu[0-9]*'):
            try:
                with open(f"{name}/cpufreq/scaling_cur_freq", "r") as _:
                    _ = _.read() #print(f"{name}/cpufreq/scaling_cur_freq {_.read()}")
            except OSError as e:
                if "Device or resource busy" in str(e):
                    continue
            ret.append(os.path.basename(name))
        ret.sort()
        return ret
#       return os.listdir('/sys/devices/system/cpu/')

    def nick(self):
        return [name.lower() for name in self.vars]

    def extract(self):
        for cpu in self.vars:
            cpu_path = f"/sys/devices/system/cpu/{cpu}"
            for line in dopen(f"{cpu_path}/cpufreq/scaling_max_freq").readlines():
                l = line.split()
                max = int(l[0])
            for line in dopen(f"{cpu_path}/cpufreq/scaling_cur_freq").readlines():
                l = line.split()
                cur = int(l[0])
            ### Need to close because of bug in sysfs (?)
            dclose(f"{cpu_path}/cpufreq/scaling_cur_freq")
            self.set1[cpu] = self.set1[cpu] + cur * 100.0 / max

            if op.update:
                self.val[cpu] = self.set1[cpu] / elapsed
            else:
                self.val[cpu] = self.set1[cpu]

            if step == op.delay:
                self.set1[cpu] = 0

# vim:ts=4:sw=4:et
