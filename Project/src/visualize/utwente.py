import utils.utwente_utils as utils

import matplotlib.pyplot as plt

def main():
    activities, teachers = utils.load_data(test=False)

    print("Average class size")
    average_class_size = utils.calculate_average_class_size(activities)
    print(average_class_size)
    utils.store_dataframe_to_csv(average_class_size, "average_class_size")

    print("Average class size per class type")
    class_type_distribution = utils.calculate_class_type_distribution(activities)
    print(class_type_distribution)
    utils.store_dataframe_to_csv(class_type_distribution, "class_type_distribution")

    print("Average class size per class type and per study")
    study_class_type_distribution = utils.calculate_study_class_type_distribution(activities)
    print(study_class_type_distribution)
    utils.store_dataframe_to_csv(study_class_type_distribution, "study_class_type_distribution")

    print("Total duration per class type")
    total_duration_per_class_type = utils.calculate_total_duration_per_class_type(activities)
    print(total_duration_per_class_type)
    utils.store_dataframe_to_csv(total_duration_per_class_type, "total_duration_per_class_type")

    print("Teacher workload")
    teacher_average_hours = utils.calculate_teacher_workload(activities, teachers)
    print(teacher_average_hours)
    utils.store_dataframe_to_csv(teacher_average_hours, "teacher_average_hours")

    print("Teacher workload per class type")
    teacher_activities = utils.calculate_teacher_class_type_distribution(activities, teachers)
    print(teacher_activities)
    utils.store_dataframe_to_csv(teacher_activities, "teacher_activities")

    print("Involement of teachers in activities")
    teacher_number_of_involvements = utils.calculate_teacher_activity_distribution(activities, teachers)
    print(teacher_number_of_involvements)
    utils.store_dataframe_to_csv(teacher_number_of_involvements, "teacher_number_of_involvements")

    print("Room usage by number of activities")
    room_usage_number_of_activities = utils.calculate_room_distribution(activities)
    print(room_usage_number_of_activities)
    utils.store_dataframe_to_csv(room_usage_number_of_activities, "room_usage_number_of_activities")

    print("Room usage by time")
    room_usage_time =  utils.calculate_room_time(activities)
    print(room_usage_time)
    utils.store_dataframe_to_csv(room_usage_time, "room_usage_time")

    print("Distribution of activities throughout the day")
    activity_distribution = utils.calculate_activity_distribution(activities)
    utils.store_dataframe_to_csv(activity_distribution, "activity_distribution")
    utils.plot_activity_distribution(activity_distribution)

    print("Distribution of activities per weekday")
    activity_distribution_day = utils.calculate_activity_distribution_by_day(activities)
    utils.store_dataframe_to_csv(activity_distribution_day, "activity_distribution_day")
    utils.plot_activity_distribution_by_day(activity_distribution_day)


if __name__ == '__main__':
    main()


