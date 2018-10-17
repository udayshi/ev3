def angle(angle,per_rotation_second):
    micro_second=per_rotation_second*1000
    output={'speed_sp':360}
    #output['speed_sp']=micro_second
    per_degree_micro_time = micro_second/360

    output['time_sp']=per_degree_micro_time*angle
    #output['360_degree_second']=output['360_degree_micro_time']/1000

    return output



print(angle(45,2))

#cloud.google.com/visionrmls
