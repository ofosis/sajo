package com.saju.saju;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class SajuController {
    @GetMapping("/")
    public String index(){
        return "common/main";
    }
    @GetMapping("result")
    public String result(){
        return "common/result";
    }



}
