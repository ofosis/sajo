using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace saju_project2.temp
{
    public class DailySaju
    {
        public UserData UserData { get; set; }
        public int Num;
        public string Direction;
        public string Color;
        public string Flavor;
        public string Fruit;
        public string Animal;
        public string BodyParts;
        public string Mind;
        public string Guide;
        public DailySaju(int num, string direction, string color, string flavor, string fruit, string animal, string bodyParts, string mind, string guide)
        {
            Num = num;
            Direction = direction;
            Color = color;
            Flavor = flavor;
            Fruit = fruit;
            Animal = animal;
            BodyParts = bodyParts;
            Mind = mind;
            Guide = guide;
        }

        public static DailySaju MakeNewSaju(string data)
        {
            var values=data.Split('\n');
            int num = Convert.ToInt32(values[0]);
            string direction = values[1];
            string color = values[2];
            string flavor = values[3];
            string fruit = values[4];
            string animal = values[5];
            string bodyparts = values[6];
            string mind = values[7];
            string guide = values[8];
            var result = new DailySaju(num,direction,color,flavor,fruit,animal,bodyparts,mind,guide);
            return result;
         }
    }
}
