class AssessmentResult:
    def __init__(
        self,
        result_id,
        user_id,
        assessment_id,
        date_taken,
        manager_id,
        score
    ):
        self.result_id = result_id
        self.user_id = user_id
        self.assessment_id = assessment_id
        self.date_taken = date_taken
        self.manager_id = manager_id
        self.score = score

    @classmethod
    def from_row(cls, row):
        """
        Expects a DB row in this order:
        (result_id, user_id, assessment_id, date_taken, manager_id, score)
        """
        return cls(
            result_id=row[0],
            user_id=row[1],
            assessment_id=row[2],
            date_taken=row[3],
            manager_id=row[4],
            score=row[5],
        )

    def __repr__(self):
        return (
            f"AssessmentResult(result_id={self.result_id}, user_id={self.user_id}, "
            f"assessment_id={self.assessment_id}, date_taken={self.date_taken}, "
            f"manager_id={self.manager_id}, score={self.score})"
        )
