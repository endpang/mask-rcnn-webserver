<?php


    $url = "http://localhost:8080/login";
    $ch = curl_init();
    $post_data = [];
    //curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    $b6 = "data:image/png;base64,";

    $post_data["hint"] = $b6.base64_encode(file_get_contents("108.png"));
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    // post数据
    curl_setopt($ch, CURLOPT_POST, 1);
    // post的变
    //echo $post_data["sketch"];
    //print_R(http_build_query($post_data));
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($post_data));

    $output = curl_exec($ch);
    $out_array = explode('*',$output);

    curl_close($ch);

print_R($output);

