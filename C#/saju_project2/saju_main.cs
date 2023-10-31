using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.TaskbarClock;
using System.Xml.Linq;
using saju_project2.temp;
using static saju_project2.temp.UserData;
using static System.Net.Mime.MediaTypeNames;
using System.Globalization;
using System.Security.Cryptography;

namespace saju_project2 {
    public partial class saju_main : Form {
        public saju_main() {
        InitializeComponent();
        }

        private void btn_result_Click_1(object sender, EventArgs e) {
            var result = python();
            var sajudata=DailySaju.MakeNewSaju(result);
            saju_result pop = new saju_result(sajudata);
            pop.ShowDialog(this);
        }
        private string python()
        {
            // 데이터 생성
            string name = tbox_name.Text;
            int year=Convert.ToInt32(cbox_year.Text);
            int month=Convert.ToInt32(cbox_month.Text);
            int day=Convert.ToInt32(cbox_day.Text);
            var time=GetBirthTime(cbox_time.SelectedIndex);
            bool isMale = cbox_gender.Text.Equals("남자") ? true : false;
            string calendar=cbox_month2.Text;
            var data = new UserData(name, year, month,day, time, isMale, calendar);

            // 데이터 직렬화
            string serializedData = data.Serialize();
            ProcessStartInfo start = new ProcessStartInfo
            {
                FileName = "python", // Python 실행 파일 경로 (시스템 경로에 있는 경우)
                WorkingDirectory = "C:\\Users\\KB\\Desktop\\test프로젝트\\TESTFILE파이썬",//파일경로
                Arguments = "test.py", // 파이썬 스크립트 파일 경로
                UseShellExecute = false,
                RedirectStandardInput = true,
                RedirectStandardOutput = true,
                CreateNoWindow = true
            };

            using (Process process = new Process())
            {
                process.StartInfo = start;
                process.Start();
                using (StreamWriter sw = process.StandardInput)
                {
                    if (sw.BaseStream.CanWrite)
                    {
                        sw.WriteLine(serializedData);
                    }
                }
                // Python 스크립트에서의 출력을 읽음
                string output = process.StandardOutput.ReadToEnd();

                process.WaitForExit();
                process.Close();

                return output;
            }
        }
    }
}
