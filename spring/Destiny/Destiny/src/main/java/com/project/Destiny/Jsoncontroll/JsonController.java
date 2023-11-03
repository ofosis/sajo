package com.project.Destiny.Jsoncontroll;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class JsonController
{
    @PostMapping("/send-json")
    public Map<String, Object> sendJsonToPythonServer(@RequestBody Map<String, String> request) {
        String name = request.get("sajuname");
        String birthyear = request.get("sajubirthyear");
        String birthmonth = request.get("sajubirthmonth");
        String birthday = request.get("sajubirthday");
        String birthtime = request.get("sajubirthtime");
        String gender = request.get("sajugender");
        String month = request.get("sajumonth");

        // JSON 데이터를 파이썬 서버에 전송하고 응답을 받는 코드
        // 파이썬 서버에서 전달된 응답을 처리하고 JSON으로 반환
        Map<String, Object> response = new HashMap<>();
        response.put("message", "Spring Boot에서 받은 텍스트: " + name + ", " + birthyear + ", " + birthmonth +"," + birthday + ", " + birthtime+", "+gender+", "+month);
        return response;
    }
}
