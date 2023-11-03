package com.project.Destiny.fortune;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class PeopleInfoDTO
{
    private String Name;
    private int BirthYear;
    private int BirthMonth;
    private int BirthDay;
    private int BirthTime;
    private boolean IsMale;
    private String Calendar;
}
