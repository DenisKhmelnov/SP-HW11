import json


def load_candidates_from_json():
    """
    :return: Возвращает список со всеми кандидатами из файла JSON
    """
    with open("candidates.json") as file:
        candidates_list = json.load(file)
        return candidates_list


def get_candidate(candidate_id):
    """
    :param candidate_id: pk, который задает пользователь
    :return: Возвращает кандидата по его pk
    """
    for candidate in load_candidates_from_json():
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    :return: Возвращает кандидата по его имени
    """
    matched_name_candidates = [candidate for candidate in load_candidates_from_json() if candidate_name in candidate["name"]]
    return matched_name_candidates


def get_candidates_by_skill(skill_name):
    """
    :param skill_name: Навык, который задаёт пользователь
    :return: Возвращает всех кандидатов у которых есть нужный навык
    """
    skilled_candidates = [candidate for candidate in load_candidates_from_json() if
                          skill_name.lower() in candidate["skills"].lower()]
    return skilled_candidates
