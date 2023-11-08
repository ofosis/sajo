using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace saju_project2.temp
{
    [Serializable]
    public class UserData
    {
        public string Name; //이름
        public int BirthYear;//출생년도
        public int BirthMonth;//출생월
        public int BirthDay;//출생일
        public int BirthTime;//출생시간
        public int isMale;//성별
        public int Calendar;//사용달력
        public UserData(string name, int birthYear, int birthMonth, int birthDay, int birthTime, int isMale, int calendar)
        {
            Name = name;
            BirthYear = birthYear;
            BirthMonth = birthMonth;
            BirthDay = birthDay;
            BirthTime = birthTime;
            this.isMale = isMale;
            Calendar = calendar;
        }

        public string Serialize()
        {
            string json = JsonConvert.SerializeObject(this);
            return json;
        }
    }
}
