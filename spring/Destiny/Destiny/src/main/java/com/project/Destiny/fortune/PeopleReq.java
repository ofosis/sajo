package com.project.Destiny.fortune;

import jakarta.annotation.Nullable;
import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class PeopleReq {
    @Nullable
    private String Name;
    @Nullable
    private int BirthYear;
    @Nullable
    private int BirthMonth;
    @Nullable
    private int BirthDay;
    @Nullable
    private int BirthTime;
    @Nullable
    private boolean IsMale;
    @Nullable
    private String Calendar;
}
