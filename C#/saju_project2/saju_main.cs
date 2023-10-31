using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace saju_project2 {
    public partial class saju_main : Form {
        public saju_main() {
        InitializeComponent();
        }

        private void btn_result_Click_1(object sender, EventArgs e) {
        saju_result pop = new saju_result();
        pop.ShowDialog(this);
        }
    }
}
